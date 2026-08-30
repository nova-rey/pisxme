from __future__ import annotations

import base64
import importlib
import json
import os
import pkgutil
import re
import shutil
import stat
import subprocess
import tempfile
import threading
import uuid
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import Any, Callable, Optional

from google.protobuf import json_format
from google.protobuf.descriptor import Descriptor, EnumDescriptor, FieldDescriptor
from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from google.protobuf.message import Message
from google.protobuf.message_factory import GetMessageClass

from kipy import KiCad
from kipy.board import Board
from kipy.board_types import (
    BoardLayer,
    BoardText,
    FootprintInstance,
    Footprint,
    Field,
    Net,
    Pad,
    PadStackShape,
    PadType,
    PST_NORMAL,
    Track,
    Via,
    ViaType,
)
from kipy.common_types import LibraryIdentifier, TextAttributes
from kipy.errors import ApiError
from kipy.geometry import Angle, Vector2
from kipy.proto.board import board_types_pb2
from kipy.proto.common.types import base_types_pb2
from kipy.proto.common.types.base_types_pb2 import DocumentType
from kipy.proto.common.types.enums_pb2 import KiCadObjectType
from kipy.util import from_mm


class BridgeError(RuntimeError):
    """An observable, user-facing bridge failure."""


def _proto(value: Any) -> Optional[Message]:
    if isinstance(value, Message):
        return value
    candidate = getattr(value, "proto", None)
    if isinstance(candidate, Message):
        return candidate
    if callable(candidate):
        candidate = candidate()
        if isinstance(candidate, Message):
            return candidate
    return None


def jsonable(value: Any) -> Any:
    """Convert KiCad wrappers/protobufs/enum-like objects into JSON-safe values."""
    message = _proto(value)
    if message is not None:
        return json_format.MessageToDict(
            message,
            preserving_proto_field_name=True,
            use_integers_for_enums=False,
        )
    if isinstance(value, Message):
        return json_format.MessageToDict(
            value,
            preserving_proto_field_name=True,
            use_integers_for_enums=False,
        )
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, bytes):
        return {"base64": base64.b64encode(value).decode("ascii")}
    if isinstance(value, Mapping):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [jsonable(v) for v in value]
    if isinstance(value, Iterable):
        return [jsonable(v) for v in value]
    if hasattr(value, "full_version"):
        return {
            "major": getattr(value, "major", None),
            "minor": getattr(value, "minor", None),
            "patch": getattr(value, "patch", None),
            "full_version": value.full_version,
        }
    return repr(value)


def enum_value(enum_cls: Any, value: Any) -> int:
    if isinstance(value, int):
        return value
    if not isinstance(value, str):
        raise BridgeError(f"Enum value must be a name or integer, got {value!r}")
    wanted = re.sub(r"[^A-Za-z0-9]", "", value).lower()
    options = enum_cls.DESCRIPTOR.values
    for option in options:
        normalized = re.sub(r"[^A-Za-z0-9]", "", option.name).lower()
        if wanted in (normalized, normalized.removeprefix("bl")):
            return option.number
    raise BridgeError(
        f"Unknown {enum_cls.DESCRIPTOR.full_name} value {value!r}; "
        f"choices are {[v.name for v in options]}"
    )


def enum_name(enum_cls: Any, value: int) -> str:
    try:
        return enum_cls.Name(value)
    except Exception:
        return str(value)


def item_id(item: Any) -> Optional[str]:
    identifier = getattr(item, "id", None)
    if isinstance(identifier, Message) and hasattr(identifier, "value"):
        return str(identifier.value)
    if isinstance(identifier, str):
        return identifier
    if identifier is not None:
        candidate = getattr(identifier, "value", None)
        if candidate:
            return str(candidate)
    raw = _proto(item)
    if raw is not None and raw.DESCRIPTOR.fields_by_name.get("id") is not None:
        raw_id = getattr(raw, "id")
        if hasattr(raw_id, "value") and raw_id.value:
            return str(raw_id.value)
    return None


def item_summary(item: Any, include_raw: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {
        "type": type(item).__name__,
        "id": item_id(item),
        "repr": repr(item),
    }
    raw = jsonable(item)
    if isinstance(raw, dict):
        result["data"] = raw
    if include_raw:
        result["raw"] = raw
    return result


def _kiid(value: str) -> Message:
    result = base_types_pb2.KIID()
    result.value = value
    return result


class ApiRegistry:
    """Discover the protobuf messages shipped by the installed kicad-python wheel."""

    def __init__(self) -> None:
        self.messages: dict[str, Descriptor] = {}
        self.enums: dict[str, EnumDescriptor] = {}
        self.modules: list[str] = []
        self._load()

    def _walk_message(self, descriptor: Descriptor) -> None:
        self.messages[descriptor.full_name] = descriptor
        for enum in descriptor.enum_types:
            self.enums[enum.full_name] = enum
        for nested in descriptor.nested_types:
            self._walk_message(nested)

    def _load(self) -> None:
        import kipy.proto as proto_root

        for module_info in pkgutil.walk_packages(proto_root.__path__, proto_root.__name__ + "."):
            try:
                module = importlib.import_module(module_info.name)
            except Exception:
                continue
            descriptor = getattr(module, "DESCRIPTOR", None)
            if descriptor is None:
                continue
            self.modules.append(module_info.name)
            for message in descriptor.message_types_by_name.values():
                self._walk_message(message)
            for enum in descriptor.enum_types_by_name.values():
                self.enums[enum.full_name] = enum

    def resolve_message(self, name: str) -> Descriptor:
        clean = name.removeprefix(".")
        if clean in ("google.protobuf.Empty", "Empty"):
            from google.protobuf.empty_pb2 import Empty

            return Empty.DESCRIPTOR
        if clean in self.messages:
            return self.messages[clean]
        matches = [d for full, d in self.messages.items() if full.endswith("." + clean)]
        if len(matches) == 1:
            return matches[0]
        raise BridgeError(
            f"Unknown or ambiguous protobuf message {name!r}; "
            f"use a fully qualified name from kicad_list_api"
        )

    def message(self, name: str, arguments: Optional[dict[str, Any]] = None) -> Message:
        descriptor = self.resolve_message(name)
        message = GetMessageClass(descriptor)()
        if arguments:
            try:
                json_format.ParseDict(arguments, message, ignore_unknown_fields=False)
            except Exception as exc:
                raise BridgeError(f"Could not populate {descriptor.full_name}: {exc}") from exc
        return message

    def describe(self, name: str) -> dict[str, Any]:
        descriptor = self.resolve_message(name)
        return {
            "full_name": descriptor.full_name,
            "file": descriptor.file.name,
            "fields": [self.describe_field(field) for field in descriptor.fields],
            "oneofs": [oneof.name for oneof in descriptor.oneofs],
        }

    @staticmethod
    def describe_field(field: FieldDescriptor) -> dict[str, Any]:
        type_name = FieldDescriptorProto.Type.Name(field.type)
        result: dict[str, Any] = {
            "name": field.name,
            "json_name": field.json_name,
            "type": type_name,
            "repeated": field.label == FieldDescriptor.LABEL_REPEATED,
            "required": field.label == FieldDescriptor.LABEL_REQUIRED,
        }
        if field.message_type is not None:
            result["message_type"] = field.message_type.full_name
        if field.enum_type is not None:
            result["enum_type"] = field.enum_type.full_name
            result["enum_values"] = [v.name for v in field.enum_type.values]
        if field.containing_oneof is not None:
            result["oneof"] = field.containing_oneof.name
        return result

    def list_api(self, prefix: str = "") -> dict[str, Any]:
        prefix = prefix.removeprefix(".")
        messages = sorted(name for name in self.messages if name.startswith(prefix))
        enums = sorted(name for name in self.enums if name.startswith(prefix))
        commands = [
            name
            for name in messages
            if ".commands." in name and name.rsplit(".", 1)[-1][0:1].isupper()
        ]
        return {
            "modules": sorted(self.modules),
            "message_count": len(messages),
            "enum_count": len(enums),
            "command_count": len(commands),
            "messages": messages,
            "enums": enums,
            "commands": commands,
        }

    def describe_method(self, request_type: str, response_type: Optional[str] = None) -> dict[str, Any]:
        request = self.resolve_message(request_type)
        inferred = response_type
        if inferred is None:
            short = request.full_name.rsplit(".", 1)[-1]
            candidates = [short + "Response", "Empty"]
            for candidate in candidates:
                try:
                    self.resolve_message(candidate)
                    inferred = candidate
                    break
                except BridgeError:
                    continue
        result = {
            "request": self.describe(request.full_name),
            "response": self.describe(inferred) if inferred else None,
            "response_inference": "name convention or Empty" if response_type is None else "explicit",
        }
        return result


class KicadSession:
    """Connection manager with socket discovery, token caching, and reconnects."""

    def __init__(self, timeout_ms: int = 5000) -> None:
        self.timeout_ms = timeout_ms
        self._lock = threading.RLock()
        self._kicad: Optional[KiCad] = None
        self._socket: Optional[str] = None
        self._token = os.environ.get("KICAD_API_TOKEN", "")

    @staticmethod
    def _socket_path(value: str) -> str:
        return value if value.startswith("ipc://") else "ipc://" + value

    def discover_sockets(self) -> list[Path]:
        values: list[Path] = []
        configured = os.environ.get("KICAD_API_SOCKET")
        if configured:
            configured = configured.removeprefix("ipc://")
            values.append(Path(configured))
        roots = [Path("/tmp/kicad")]
        tmpdir = os.environ.get("TMPDIR")
        if tmpdir:
            roots.append(Path(tmpdir) / "kicad")
        for root in roots:
            if not root.is_dir():
                continue
            values.extend(sorted(root.glob("api.sock*"), key=lambda p: p.stat().st_mtime, reverse=True))
        unique: list[Path] = []
        seen: set[str] = set()
        for path in values:
            try:
                mode = path.stat().st_mode
            except OSError:
                continue
            if not stat.S_ISSOCK(mode):
                continue
            text = str(path)
            if text not in seen:
                seen.add(text)
                unique.append(path)
        return unique

    def _close(self) -> None:
        if self._kicad is not None:
            client = getattr(self._kicad, "_client", None)
            if client is not None:
                try:
                    client.close()
                except Exception:
                    pass
        self._kicad = None
        self._socket = None

    def connect(self) -> KiCad:
        with self._lock:
            if self._kicad is not None:
                try:
                    self._kicad.ping()
                    return self._kicad
                except Exception:
                    self._close()

            sockets = self.discover_sockets()
            if not sockets:
                raise BridgeError(
                    "KiCad IPC is unavailable: no Unix socket was found. "
                    "Start KiCad, open PCB Editor, and enable Preferences > Plugins > "
                    "Enable KiCad API. Expected /tmp/kicad/api.sock."
                )
            errors: list[str] = []
            for path in sockets:
                candidate: Optional[KiCad] = None
                try:
                    candidate = KiCad(
                        socket_path=self._socket_path(str(path)),
                        kicad_token=self._token,
                        timeout_ms=self.timeout_ms,
                    )
                    candidate.get_version()
                    self._kicad = candidate
                    self._socket = str(path)
                    token = getattr(getattr(candidate, "_client", None), "_kicad_token", None)
                    if token:
                        self._token = token
                    return candidate
                except Exception as exc:
                    errors.append(f"{path}: {type(exc).__name__}: {exc}")
                    if candidate is not None:
                        client = getattr(candidate, "_client", None)
                        if client is not None:
                            try:
                                client.close()
                            except Exception:
                                pass
            raise BridgeError("KiCad IPC connection failed: " + " | ".join(errors))

    def call(self, operation: Callable[[KiCad], Any]) -> Any:
        with self._lock:
            for attempt in range(2):
                kicad = self.connect()
                try:
                    return operation(kicad)
                except ApiError as exc:
                    raise BridgeError(f"KiCad API error: {exc}") from exc
                except Exception as exc:
                    if attempt == 0 and ("connect" in str(exc).lower() or "receive" in str(exc).lower()):
                        self._close()
                        continue
                    raise BridgeError(f"KiCad operation failed: {type(exc).__name__}: {exc}") from exc
        raise BridgeError("KiCad operation failed after reconnect")

    def status(self, probe: bool = True) -> dict[str, Any]:
        sockets = self.discover_sockets()
        result: dict[str, Any] = {
            "socket_candidates": [str(p) for p in sockets],
            "configured_socket": os.environ.get("KICAD_API_SOCKET"),
            "token_configured": bool(self._token),
            "connected": False,
            "socket": self._socket,
            "live_version": None,
            "error": None,
            "pcb_editor_required": True,
            "headless_api_server_supported_by_installed_cli": False,
        }
        try:
            probe_process = subprocess.run(
                ["pgrep", "-f", "/Applications/KiCad/KiCad.app/Contents/(MacOS/kicad|Applications/pcbnew.app)"],
                capture_output=True,
                text=True,
                check=False,
            )
            result["kicad_process_detected"] = bool(probe_process.stdout.strip())
        except OSError:
            result["kicad_process_detected"] = None
        if probe:
            try:
                version = self.call(lambda k: k.get_version())
                result["connected"] = True
                result["socket"] = self._socket
                result["live_version"] = jsonable(version)
                result["token_configured"] = bool(self._token)
            except BridgeError as exc:
                result["error"] = str(exc)
        return result

    def board(self) -> Board:
        def get(kicad: KiCad) -> Board:
            try:
                return kicad.get_board()
            except Exception as exc:
                raise BridgeError(
                    "The KiCad IPC server is reachable, but no PCB editor/document is open: "
                    f"{exc}"
                ) from exc

        return self.call(get)

    def raw_call(self, request: Message, response_type: type[Message]) -> Message:
        return self.call(lambda k: k._client.send(request, response_type))


class CliRunner:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.path = os.environ.get(
            "KICAD_CLI_PATH", "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
        )

    def _run(self, args: Sequence[str], timeout: int = 120) -> dict[str, Any]:
        command = [self.path, *[str(a) for a in args]]
        try:
            completed = subprocess.run(
                command,
                cwd=str(self.root),
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
        except FileNotFoundError as exc:
            raise BridgeError(f"kicad-cli not found at {self.path}") from exc
        except subprocess.TimeoutExpired as exc:
            raise BridgeError(f"kicad-cli timed out after {timeout}s: {' '.join(command)}") from exc
        return {
            "command": command,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "succeeded": completed.returncode == 0,
        }

    def version(self) -> dict[str, Any]:
        result = self._run(["--version"])
        result["version"] = result["stdout"].strip()
        return result

    def help(self, args: Sequence[str]) -> dict[str, Any]:
        return self._run([*args, "--help"])

    @staticmethod
    def _read_report(path: Optional[Path]) -> Any:
        if path is None or not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return path.read_text(encoding="utf-8", errors="replace")

    def validate(
        self,
        kind: str,
        input_file: Path,
        output_file: Optional[Path],
        report_format: str = "json",
        extra_args: Optional[Sequence[str]] = None,
        timeout: int = 120,
    ) -> dict[str, Any]:
        if kind not in {"drc", "erc"}:
            raise BridgeError("Validation kind must be 'drc' or 'erc'")
        temp_dir: Optional[tempfile.TemporaryDirectory[str]] = None
        report_path = output_file
        if report_path is None:
            temp_dir = tempfile.TemporaryDirectory(prefix="kicad-codex-")
            report_path = Path(temp_dir.name) / f"{kind}.{report_format}"
        args = ["pcb" if kind == "drc" else "sch", kind, "--format", report_format, "--output", str(report_path)]
        if extra_args:
            args.extend(str(a) for a in extra_args)
        args.append(str(input_file))
        try:
            result = self._run(args, timeout=timeout)
            result["input_file"] = str(input_file)
            result["report_file"] = str(output_file) if output_file else None
            result["report"] = self._read_report(report_path)
            return result
        finally:
            if temp_dir is not None:
                temp_dir.cleanup()

    def export(
        self,
        kind: str,
        input_file: Path,
        output: Path,
        extra_args: Optional[Sequence[str]] = None,
        timeout: int = 180,
    ) -> dict[str, Any]:
        board_ops = {
            "gerbers", "drill", "pos", "pdf", "svg", "step", "stepz", "stl", "glb",
            "odb", "ipc2581", "ipcd356", "gencad", "dxf", "ps", "stats", "3dpdf",
        }
        schematic_ops = {"bom", "dxf", "hpgl", "netlist", "pdf", "ps", "svg", "python-bom"}
        if kind in board_ops:
            args = ["pcb", "export", kind, "--output", str(output)]
        elif kind in schematic_ops:
            args = ["sch", "export", kind, "--output", str(output)]
        else:
            raise BridgeError(f"Unsupported KiCad 10 export operation {kind!r}")
        if extra_args:
            args.extend(str(a) for a in extra_args)
        args.append(str(input_file))
        result = self._run(args, timeout=timeout)
        result.update({"input_file": str(input_file), "output": str(output), "operation": kind})
        result["output_exists"] = output.exists()
        return result


class FileScope:
    def __init__(self, root: Optional[str] = None) -> None:
        configured = root or os.environ.get("KICAD_PROJECT_ROOT") or os.getcwd()
        self.root = Path(configured).expanduser().resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def resolve(self, value: str, must_exist: bool = False) -> Path:
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = self.root / path
        resolved = path.resolve(strict=False)
        try:
            resolved.relative_to(self.root)
        except ValueError as exc:
            raise BridgeError(f"Path is outside configured KiCad project root {self.root}: {value}") from exc
        if must_exist and not resolved.exists():
            raise BridgeError(f"KiCad project path does not exist: {resolved}")
        return resolved

    def write(self, path: str, content: str, encoding: str = "utf-8") -> dict[str, Any]:
        target = self.resolve(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, temp_name = tempfile.mkstemp(prefix=f".{target.name}.", dir=str(target.parent))
        try:
            with os.fdopen(fd, "w", encoding=encoding, newline="") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_name, target)
        except Exception:
            try:
                os.unlink(temp_name)
            except OSError:
                pass
            raise
        return {"path": str(target), "bytes": target.stat().st_size}


def _board_items(board: Board, kind: str) -> Sequence[Any]:
    methods = {
        "footprints": board.get_footprints,
        "pads": board.get_pads,
        "tracks": board.get_tracks,
        "vias": board.get_vias,
        "zones": board.get_zones,
        "graphics": board.get_shapes,
        "text": board.get_text,
        "dimensions": board.get_dimensions,
        "barcodes": board.get_barcodes,
        "reference_images": board.get_reference_images,
        "groups": board.get_groups,
    }
    if kind not in methods:
        raise BridgeError(f"Unknown board item collection {kind!r}; choices are {sorted(methods)}")
    return methods[kind]()


def _new_text(value: str, x_mm: float, y_mm: float, layer: Any, size_mm: float, thickness_mm: float) -> BoardText:
    text = BoardText()
    text.value = value
    text.position = Vector2.from_xy_mm(x_mm, y_mm)
    text.layer = enum_value(BoardLayer, layer)
    attributes = TextAttributes()
    attributes.size = Vector2.from_xy_mm(size_mm, size_mm)
    attributes.stroke_width = from_mm(thickness_mm)
    attributes.visible = True
    attributes.keep_upright = True
    text.attributes = attributes
    return text


def _new_footprint(
    reference: str,
    value: str,
    x_mm: float,
    y_mm: float,
    pad_count: int = 2,
    pad_pitch_mm: float = 2.54,
) -> FootprintInstance:
    if pad_count < 1 or pad_count > 64:
        raise BridgeError("pad_count must be between 1 and 64")
    instance = FootprintInstance()
    instance.position = Vector2.from_xy_mm(x_mm, y_mm)
    instance.layer = enum_value(BoardLayer, "BL_F_Cu")
    instance.orientation = Angle.from_degrees(0)
    instance.definition.id = LibraryIdentifier()
    instance.definition.id.library = "Codex"
    instance.definition.id.name = "Codex_Custom"

    ref_field = instance.reference_field
    ref_field.name = "Reference"
    ref_field.text.value = reference
    ref_field.text.position = Vector2.from_xy_mm(x_mm, y_mm - 1.5)
    ref_field.visible = True
    value_field = instance.value_field
    value_field.name = "Value"
    value_field.text.value = value
    value_field.text.position = Vector2.from_xy_mm(x_mm, y_mm + 1.5)
    value_field.visible = True

    for index in range(pad_count):
        pad = Pad()
        pad.number = str(index + 1)
        pad.pad_type = PadType.PT_SMD
        pad.position = Vector2.from_xy_mm(
            x_mm + (index - (pad_count - 1) / 2) * pad_pitch_mm,
            y_mm,
        )
        pad.padstack.type = PST_NORMAL
        copper = pad.padstack.copper_layer(enum_value(BoardLayer, "BL_F_Cu"))
        if copper is None:
            raise BridgeError("KiCad returned no front copper layer for a normal padstack")
        copper.shape = PadStackShape.PSS_RECTANGLE if index == 0 else PadStackShape.PSS_ROUNDRECT
        copper.size = Vector2.from_xy_mm(1.5, 1.5)
        instance.definition.add_item(pad)
    return instance


def _infer_response_type(registry: ApiRegistry, request_type: str) -> str:
    short = request_type.rsplit(".", 1)[-1]
    for candidate in (short + "Response", "Empty"):
        try:
            registry.resolve_message(candidate)
            return candidate
        except BridgeError:
            pass
    raise BridgeError(f"No response type was inferred for {request_type!r}; pass response_type explicitly")
