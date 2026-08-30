"""Scoped schematic authoring backend for the Codex KiCad bridge.

The PCB backend remains the KiCad IPC implementation in :mod:`bridge.core`.
This module deliberately keeps schematic authoring behind a small adapter so
the bridge does not grow a second KiCad file-format implementation.  The
adapter uses ``kicad-sch-api`` for parsing and object manipulation, and uses a
temporary file plus a parse-after-write check before replacing a target.

The dependency is imported lazily.  PCB-only deployments therefore retain the
same import and startup behaviour when the optional schematic dependency has
not been installed.
"""

from __future__ import annotations

import hashlib
import importlib
import json
import os
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Optional

from .core import BridgeError


def _load_library() -> Any:
    """Load the supported schematic library with an actionable error."""

    try:
        return importlib.import_module("kicad_sch_api")
    except ImportError as exc:
        raise BridgeError(
            "Schematic authoring requires kicad-sch-api; install the bridge "
            "requirements before using schematic tools"
        ) from exc


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _issues_to_dict(issues: Any) -> list[dict[str, Any]]:
    """Convert kicad-sch-api validation objects into stable JSON values."""

    def normalize(value: Any) -> Any:
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, dict):
            return {str(key): normalize(item) for key, item in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [normalize(item) for item in value]
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        return str(value)

    result: list[dict[str, Any]] = []
    for issue in issues or []:
        if isinstance(issue, dict):
            result.append(normalize(issue))
            continue
        data = getattr(issue, "__dict__", None)
        if isinstance(data, dict):
            result.append(normalize(data))
            continue
        result.append({"message": str(issue)})
    return result


@dataclass
class SchematicDocument:
    """A loaded schematic and its source provenance."""

    schematic: Any
    path: Path
    source_sha256: str

    def info(self) -> dict[str, Any]:
        """Return source identity and library statistics."""

        return {
            "path": str(self.path),
            "source_sha256": self.source_sha256,
            "statistics": self.schematic.get_statistics(),
        }

    def validate(self) -> dict[str, Any]:
        """Run library-level structural validation without changing the file."""

        issues = _issues_to_dict(self.schematic.validate())
        errors = [issue for issue in issues if issue.get("level") in {"error", "critical"}]
        return {"valid": not errors, "issues": issues, "error_count": len(errors)}

    def save(
        self,
        target: Optional[str | Path] = None,
        *,
        validate: bool = True,
        reopen: bool = True,
    ) -> dict[str, Any]:
        """Atomically save the schematic after a parse-after-write check.

        The library writes only a temporary sibling.  The original target is
        replaced after the temporary output can be loaded again.  If any
        operation fails, the original target remains untouched.
        """

        destination = Path(target) if target is not None else self.path
        destination = destination.expanduser().resolve()
        if destination.suffix != ".kicad_sch":
            raise BridgeError(f"Schematic target must end in .kicad_sch: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)

        if validate:
            result = self.validate()
            if not result["valid"]:
                raise BridgeError(f"Schematic validation failed: {result['issues']}")

        fd, temp_name = tempfile.mkstemp(
            prefix=f".{destination.stem}.codex-", suffix=".kicad_sch", dir=str(destination.parent)
        )
        temp_path = Path(temp_name)
        os.close(fd)
        try:
            self.schematic.save(temp_path, preserve_format=True)
            if reopen:
                # Re-opening is intentionally done through the same supported
                # backend, not by accepting bytes merely because they exist.
                reopened = type(self.schematic).load(temp_path)
                if validate:
                    reopened_issues = _issues_to_dict(reopened.validate())
                    reopened_errors = [
                        issue for issue in reopened_issues if issue.get("level") in {"error", "critical"}
                    ]
                    if reopened_errors:
                        raise BridgeError(f"Reopened schematic validation failed: {reopened_errors}")
            os.replace(temp_path, destination)
        except Exception as exc:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass
            if isinstance(exc, BridgeError):
                raise
            raise BridgeError(f"Schematic save failed; original was not replaced: {exc}") from exc

        # Keep the in-memory object associated with the committed disposable
        # copy, but do not silently update source provenance before replacement.
        self.path = destination
        self.source_sha256 = _sha256(destination)
        return {"path": str(destination), "sha256": self.source_sha256, "bytes": destination.stat().st_size}

    def save_and_native_validate(
        self,
        destination: str | Path,
        runner: Any,
        *,
        baseline: Optional[dict[str, Any]] = None,
        export_netlist: Optional[str | Path] = None,
        timeout: int = 120,
    ) -> dict[str, Any]:
        """Validate a candidate with KiCad before replacing the destination.

        The direct-library checks are followed by a native KiCad ERC on the
        temporary candidate.  The destination is replaced only when KiCad
        can parse the file and the candidate introduces no new ERC errors
        relative to ``baseline``.  This keeps legacy schematics usable while
        preventing an invalid generated file from being promoted silently.
        """

        target = Path(destination).expanduser().resolve()
        if target.suffix != ".kicad_sch":
            raise BridgeError(f"Schematic target must end in .kicad_sch: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        direct = self.validate()
        if not direct["valid"]:
            raise BridgeError(f"Schematic validation failed: {direct['issues']}")

        fd, temp_name = tempfile.mkstemp(
            prefix=f".{target.stem}.codex-", suffix=".kicad_sch", dir=str(target.parent)
        )
        candidate = Path(temp_name)
        report_path = candidate.with_suffix(".erc.json")
        try:
            os.close(fd)
            self.schematic.save(candidate, preserve_format=True)
            reopened = type(self.schematic).load(candidate)
            reopened_issues = _issues_to_dict(reopened.validate())
            reopened_errors = [
                issue for issue in reopened_issues if issue.get("level") in {"error", "critical"}
            ]
            if reopened_errors:
                raise BridgeError(f"Reopened schematic validation failed: {reopened_errors}")

            native = runner.validate("erc", candidate, report_path, "json", timeout=timeout)
            report = native.get("report")
            if not isinstance(report, dict):
                raise BridgeError(
                    "KiCad native ERC did not produce a readable JSON report; "
                    f"returncode={native.get('returncode')} stderr={native.get('stderr', '')}"
                )
            delta = native_violation_delta(baseline, report)
            native["violation_delta"] = delta
            if native.get("returncode") != 0:
                return {
                    "promoted": False,
                    "path": str(target),
                    "native_erc": native,
                    "reason": "native_erc_command_failed",
                }
            if delta["introduced_error_count"]:
                return {
                    "promoted": False,
                    "path": str(target),
                    "native_erc": native,
                    "reason": "introduced_native_erc_errors",
                }

            netlist_result = None
            if export_netlist is not None:
                netlist_target = Path(export_netlist).expanduser().resolve()
                netlist_target.parent.mkdir(parents=True, exist_ok=True)
                netlist_result = runner.export("netlist", candidate, netlist_target, timeout=timeout)
                if not netlist_result.get("succeeded") or not netlist_result.get("output_exists"):
                    raise BridgeError(
                        "KiCad native netlist export failed; original target was not replaced: "
                        f"{netlist_result}"
                    )

            os.replace(candidate, target)
            self.path = target
            self.source_sha256 = _sha256(target)
            return {
                "promoted": True,
                "path": str(target),
                "sha256": self.source_sha256,
                "native_erc": native,
                "netlist": netlist_result,
            }
        except Exception:
            candidate.unlink(missing_ok=True)
            report_path.unlink(missing_ok=True)
            raise
        finally:
            report_path.unlink(missing_ok=True)


def native_violation_delta(
    baseline: Optional[dict[str, Any]], candidate: dict[str, Any]
) -> dict[str, Any]:
    """Return deterministic native ERC error delta for a baseline report."""

    def records(report: Optional[dict[str, Any]]) -> list[dict[str, Any]]:
        found: list[dict[str, Any]] = []
        for sheet in (report or {}).get("sheets", []):
            sheet_path = sheet.get("path", "")
            for violation in sheet.get("violations", []):
                if violation.get("severity") not in {"error", "critical"}:
                    continue
                found.append({"sheet": sheet_path, "violation": violation})
        return found

    baseline_records = records(baseline)
    candidate_records = records(candidate)
    counts: dict[str, int] = {}
    for item in baseline_records:
        key = json.dumps(item, sort_keys=True, separators=(",", ":"))
        counts[key] = counts.get(key, 0) + 1
    introduced: list[dict[str, Any]] = []
    for item in candidate_records:
        key = json.dumps(item, sort_keys=True, separators=(",", ":"))
        if counts.get(key, 0):
            counts[key] -= 1
        else:
            introduced.append(item)
    return {
        "baseline_error_count": len(baseline_records),
        "candidate_error_count": len(candidate_records),
        "introduced_error_count": len(introduced),
        "introduced_errors": introduced,
        "baseline_provided": baseline is not None,
    }


class SchematicBackend:
    """Small stable bridge-facing adapter around kicad-sch-api."""

    def __init__(self, library_loader: Callable[[], Any] = _load_library) -> None:
        self._library_loader = library_loader

    def open(self, path: str | Path) -> SchematicDocument:
        source = Path(path).expanduser().resolve()
        if source.suffix != ".kicad_sch":
            raise BridgeError(f"Schematic source must end in .kicad_sch: {source}")
        if not source.is_file():
            raise BridgeError(f"Schematic source does not exist: {source}")
        library = self._library_loader()
        # Project-local symbol libraries are not part of KiCad's global
        # cache.  Register sibling .kicad_sym files before callers add or
        # inspect custom symbols (for example PiSXMe:CM5_B2B_100).  Loading
        # remains read-only; this only configures the disposable library
        # cache used by kicad-sch-api.
        cache_getter = getattr(library, "get_symbol_cache", None)
        if callable(cache_getter):
            cache = cache_getter()
            candidates = sorted(source.parent.glob("*.kicad_sym"))
            for candidate in candidates:
                try:
                    cache.add_library_path(str(candidate))
                except Exception as exc:
                    raise BridgeError(
                        f"Could not register project symbol library {candidate}: {exc}"
                    ) from exc
        try:
            schematic = library.load_schematic(str(source))
        except Exception as exc:
            raise BridgeError(f"Could not load schematic {source}: {exc}") from exc
        return SchematicDocument(schematic, source, _sha256(source))

    def create(self, name: str = "Untitled") -> SchematicDocument:
        library = self._library_loader()
        try:
            schematic = library.create_schematic(name)
        except Exception as exc:
            raise BridgeError(f"Could not create schematic {name!r}: {exc}") from exc
        # Unsaved documents have no source hash.  A caller must supply a target
        # to save(), which is the safe boundary for a new source file.
        return SchematicDocument(schematic, Path("<unsaved>"), "")

    def add_symbol_library(self, path: str | Path) -> dict[str, Any]:
        """Register a project-local ``.kicad_sym`` with kicad-sch-api.

        The cache is process-global inside the third-party library, so callers
        should register a project library before adding symbols from it.  The
        file is parsed by that library; no pin mapping is inferred here.
        """

        library_path = Path(path).expanduser().resolve()
        if library_path.suffix != ".kicad_sym" or not library_path.is_file():
            raise BridgeError(f"Project symbol library does not exist: {library_path}")
        library = self._library_loader()
        try:
            cache = library.get_symbol_cache()
            cache.add_library_path(str(library_path))
        except Exception as exc:
            raise BridgeError(f"Could not register symbol library {library_path}: {exc}") from exc
        return {"path": str(library_path), "sha256": _sha256(library_path)}

    @staticmethod
    def add_symbol(document: SchematicDocument, **kwargs: Any) -> Any:
        return document.schematic.components.add(**kwargs)

    @staticmethod
    def remove_symbol(document: SchematicDocument, reference: str) -> bool:
        return bool(document.schematic.components.remove(reference))

    @staticmethod
    def set_symbol_property(document: SchematicDocument, reference: str, name: str, value: str) -> None:
        component = document.schematic.components.get(reference)
        if component is None:
            raise BridgeError(f"Unknown schematic component {reference!r}")
        component.set_property(name, value)

    @staticmethod
    def set_footprint(document: SchematicDocument, reference: str, footprint: str) -> None:
        component = document.schematic.components.get(reference)
        if component is None:
            raise BridgeError(f"Unknown schematic component {reference!r}")
        component.footprint = footprint

    @staticmethod
    def move_symbol(document: SchematicDocument, reference: str, position: tuple[float, float]) -> None:
        component = document.schematic.components.get(reference)
        if component is None:
            raise BridgeError(f"Unknown schematic component {reference!r}")
        component.move(*position)

    @staticmethod
    def rotate_symbol(document: SchematicDocument, reference: str, rotation: float) -> None:
        component = document.schematic.components.get(reference)
        if component is None:
            raise BridgeError(f"Unknown schematic component {reference!r}")
        component.rotate(rotation)

    @staticmethod
    def get_pins(document: SchematicDocument, reference: str) -> list[dict[str, Any]]:
        component = document.schematic.components.get(reference)
        if component is None:
            raise BridgeError(f"Unknown schematic component {reference!r}")
        result = []
        for pin in component.list_pins():
            record = dict(pin)
            position = record.get("position")
            if position is not None and hasattr(position, "x") and hasattr(position, "y"):
                record["position"] = {"x": position.x, "y": position.y}
            result.append(record)
        return result

    @staticmethod
    def get_pin_position(document: SchematicDocument, reference: str, pin: str) -> Any:
        return document.schematic.get_component_pin_position(reference, pin)

    @staticmethod
    def connect_pins(document: SchematicDocument, first: tuple[str, str], second: tuple[str, str]) -> Any:
        return document.schematic.add_wire_between_pins(first[0], first[1], second[0], second[1])

    @staticmethod
    def add_wire(document: SchematicDocument, start: tuple[float, float], end: tuple[float, float]) -> str:
        return document.schematic.add_wire(start, end)

    @staticmethod
    def remove_wire(document: SchematicDocument, wire_uuid: str) -> bool:
        return bool(document.schematic.wires.remove(wire_uuid))

    @staticmethod
    def add_junction(document: SchematicDocument, position: tuple[float, float]) -> str:
        return document.schematic.junctions.add(position)

    @staticmethod
    def add_label(document: SchematicDocument, text: str, position: tuple[float, float], **kwargs: Any) -> str:
        return document.schematic.add_label(text, position=position, **kwargs)

    @staticmethod
    def add_global_label(document: SchematicDocument, text: str, position: tuple[float, float], **kwargs: Any) -> str:
        return document.schematic.add_global_label(text, position=position, **kwargs)

    @staticmethod
    def add_hierarchical_label(document: SchematicDocument, text: str, position: tuple[float, float], **kwargs: Any) -> str:
        return document.schematic.add_hierarchical_label(text, position=position, **kwargs)

    @staticmethod
    def add_sheet(document: SchematicDocument, **kwargs: Any) -> str:
        return document.schematic.add_sheet(**kwargs)

    @staticmethod
    def remove_sheet(document: SchematicDocument, sheet_uuid: str) -> bool:
        return bool(document.schematic.remove_sheet(sheet_uuid))

    @staticmethod
    def add_sheet_pin(document: SchematicDocument, **kwargs: Any) -> str:
        return document.schematic.add_sheet_pin(**kwargs)

    @staticmethod
    def add_no_connect(document: SchematicDocument, position: tuple[float, float]) -> Any:
        return document.schematic.no_connects.add(position)

    @staticmethod
    def remove_no_connect(document: SchematicDocument, marker_uuid: str) -> bool:
        return bool(document.schematic.no_connects.remove(marker_uuid))

    @staticmethod
    def list_sheets(document: SchematicDocument) -> Any:
        return document.schematic.sheets.get_sheet_hierarchy()

    @staticmethod
    def validate_hierarchy(document: SchematicDocument) -> dict[str, Any]:
        issues = _issues_to_dict(document.schematic.hierarchy.validate())
        sheet_issues = _issues_to_dict(document.schematic.sheets.validate())
        return {"valid": not issues and not sheet_issues, "hierarchy": issues, "sheets": sheet_issues}

    @staticmethod
    def find_unconnected_pins(document: SchematicDocument) -> Any:
        issues = _issues_to_dict(document.schematic.validate())
        return [issue for issue in issues if issue.get("category") == "connectivity"]

    @staticmethod
    def connectivity_report(document: SchematicDocument) -> Any:
        return document.schematic.get_statistics()

    def search_symbols(self, pattern: str) -> Any:
        library = self._library_loader()
        search = getattr(library, "search_symbols", None)
        if not callable(search):
            raise BridgeError("kicad-sch-api does not expose symbol search")
        results = search(pattern)
        return [getattr(item, "model_dump", lambda: getattr(item, "to_dict", lambda: str(item))())() for item in results]

    def get_symbol(self, lib_id: str) -> Any:
        library = self._library_loader()
        getter = getattr(library, "get_symbol_info", None)
        if not callable(getter):
            raise BridgeError("kicad-sch-api does not expose symbol lookup")
        symbol = getter(lib_id)
        if symbol is None:
            raise BridgeError(f"Symbol {lib_id!r} was not found")
        if hasattr(symbol, "model_dump"):
            return symbol.model_dump()
        if hasattr(symbol, "to_dict"):
            return symbol.to_dict()
        return str(symbol)

    @staticmethod
    def trace_net(document: SchematicDocument, reference: str, pin: str) -> Any:
        return document.schematic.get_connected_pins(reference, pin)

    @staticmethod
    def list_nets(document: SchematicDocument) -> Any:
        records = []
        for net in document.schematic.nets:
            to_dict = getattr(net, "to_dict", None)
            records.append(to_dict() if callable(to_dict) else {"name": getattr(net, "name", str(net))})
        return records
