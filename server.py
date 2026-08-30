from __future__ import annotations

import json
import os
import base64
import subprocess
import uuid
from functools import wraps
from pathlib import Path
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from bridge.core import (
    ApiRegistry,
    BridgeError,
    CliRunner,
    FileScope,
    KicadSession,
    _board_items,
    _infer_response_type,
    _kiid,
    _new_footprint,
    _new_text,
    enum_name,
    enum_value,
    item_id,
    item_summary,
    jsonable,
)
from bridge.schematic_backend import SchematicBackend, SchematicDocument
from kipy.board_types import (
    BoardCircle,
    BoardLayer,
    BoardRectangle,
    BoardSegment,
    BoardText,
    FootprintInstance,
    Net,
    Track,
    Via,
    ViaType,
)
from kipy.common_types import GraphicAttributes, TextAttributes
from kipy.geometry import Angle, Vector2
from kipy.proto.board import board_commands_pb2, board_types_pb2
from kipy.proto.common.commands import editor_commands_pb2, project_commands_pb2
from kipy.proto.common.types import base_types_pb2
from kipy.proto.common.types.base_types_pb2 import DocumentType, MapMergeMode
from kipy.proto.common.types.enums_pb2 import KiCadObjectType
from kipy.util import from_mm
from google.protobuf.empty_pb2 import Empty


ROOT = os.environ.get("KICAD_PROJECT_ROOT") or os.getcwd()
scope = FileScope(ROOT)
session = KicadSession(timeout_ms=int(os.environ.get("KICAD_IPC_TIMEOUT_MS", "5000")))
cli = CliRunner(scope.root)
registry = ApiRegistry()
schematic_backend = SchematicBackend()
schematic_documents: dict[str, SchematicDocument] = {}

mcp = FastMCP(
    "kicad-codex-bridge",
    instructions=(
        "Use official KiCad IPC through kicad-python for live PCB work. "
        "Check kicad_connection_status before writes. Live IPC requires KiCad's GUI PCB editor "
        "and the enabled API server. Use kicad_drc/kicad_erc or kicad_cli_export for validation "
        "and manufacturing outputs. Schematic authoring uses the scoped direct .kicad_sch backend "
        "and must be followed by native KiCad ERC/parity validation. All API errors are returned."
    ),
)


def _tool_error(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except BridgeError:
            raise
        except Exception as exc:
            raise BridgeError(f"{fn.__name__} failed: {type(exc).__name__}: {exc}") from exc

    return wrapped


def _doc_dict(doc: Any) -> dict[str, Any]:
    return jsonable(doc)


@mcp.tool()
@_tool_error
def kicad_connection_status(probe: bool = True) -> dict[str, Any]:
    """Discover KiCad IPC sockets and optionally perform a live version handshake."""
    return session.status(probe=probe)


@mcp.tool()
@_tool_error
def kicad_get_version() -> dict[str, Any]:
    """Return live KiCad version when IPC is available, plus the installed CLI version."""
    result: dict[str, Any] = {"installed_cli": cli.version(), "live": None}
    try:
        result["live"] = jsonable(session.call(lambda k: k.get_version()))
    except BridgeError as exc:
        result["live_error"] = str(exc)
    return result


@mcp.tool()
@_tool_error
def kicad_list_open_documents() -> dict[str, Any]:
    """List open KiCad documents by type through the live IPC server."""
    def collect(kicad):
        docs = []
        for doc_type in DocumentType.DESCRIPTOR.values:
            if doc_type.name == "DOCTYPE_UNKNOWN":
                continue
            try:
                found = kicad.get_open_documents(doc_type.number)
            except Exception as exc:
                docs.append({"type": doc_type.name, "error": str(exc)})
                continue
            docs.extend({"type": doc_type.name, "document": _doc_dict(doc)} for doc in found)
        return docs

    return {"documents": session.call(collect)}


@mcp.tool()
@_tool_error
def kicad_get_active_document() -> dict[str, Any]:
    """Return open documents and explain that KiCad 10 IPC does not expose active-document identity."""
    docs = kicad_list_open_documents()
    docs["active_document"] = None
    docs["limitation"] = "The installed KiCad 10 IPC messages expose open documents, not active-document identity."
    return docs


@mcp.tool()
@_tool_error
def kicad_open_file(path: str) -> dict[str, Any]:
    """Open a scoped KiCad project/board/schematic with the native macOS application association."""
    target = scope.resolve(path, must_exist=True)
    suffix = target.suffix.lower()
    if suffix not in {".kicad_pro", ".kicad_pcb", ".kicad_sch", ".kicad_sym", ".kicad_mod"}:
        raise BridgeError(f"Not a recognized KiCad design file: {target}")
    completed = __import__("subprocess").run(["open", str(target)], capture_output=True, text=True, check=False)
    return {"path": str(target), "returncode": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}


def _schematic_document(path: str) -> tuple[Path, SchematicDocument]:
    target = scope.resolve(path, must_exist=True)
    if target.suffix.lower() != ".kicad_sch":
        raise BridgeError(f"Not a KiCad schematic: {target}")
    key = str(target)
    document = schematic_documents.get(key)
    if document is None:
        document = schematic_backend.open(target)
        schematic_documents[key] = document
    return target, document


@mcp.tool()
@_tool_error
def kicad_sch_open(path: str) -> dict[str, Any]:
    """Load a scoped .kicad_sch through the direct schematic backend."""
    target = scope.resolve(path, must_exist=True)
    if target.suffix.lower() != ".kicad_sch":
        raise BridgeError(f"Not a KiCad schematic: {target}")
    document = schematic_backend.open(target)
    schematic_documents[str(target)] = document
    return document.info()


@mcp.tool()
@_tool_error
def kicad_sch_create(name: str = "Untitled", path: Optional[str] = None) -> dict[str, Any]:
    """Create a new in-memory schematic, optionally saving it atomically to a scoped path."""
    document = schematic_backend.create(name)
    if path is None:
        raise BridgeError("A scoped .kicad_sch path is required for a durable schematic")
    target = scope.resolve(path)
    if target.suffix.lower() != ".kicad_sch":
        raise BridgeError(f"Not a KiCad schematic target: {target}")
    document.save(target, validate=False)
    schematic_documents[str(target)] = document
    return document.info()


@mcp.tool()
@_tool_error
def kicad_sch_get_info(path: str) -> dict[str, Any]:
    """Return schematic source identity and object statistics."""
    return _schematic_document(path)[1].info()


@mcp.tool()
@_tool_error
def kicad_sch_validate(path: str) -> dict[str, Any]:
    """Run direct-library structural validation; use kicad_erc for native KiCad ERC."""
    return _schematic_document(path)[1].validate()


@mcp.tool()
@_tool_error
def kicad_sch_add_symbol_library(path: str) -> dict[str, Any]:
    """Register a project-local .kicad_sym library before adding custom symbols."""
    target = scope.resolve(path, must_exist=True)
    return schematic_backend.add_symbol_library(target)


@mcp.tool()
@_tool_error
def kicad_sch_save(path: str, target: Optional[str] = None, validate: bool = True) -> dict[str, Any]:
    """Atomically save an open schematic after direct-library parse/reopen validation."""
    source, document = _schematic_document(path)
    destination = scope.resolve(target) if target else source
    result = document.save(destination, validate=validate)
    schematic_documents[str(destination)] = document
    if destination != source:
        schematic_documents.pop(str(source), None)
    return result


@mcp.tool()
@_tool_error
def kicad_sch_save_and_validate(
    path: str,
    target: Optional[str] = None,
    baseline_erc: Optional[str] = None,
    netlist_output: Optional[str] = None,
    timeout: int = 120,
) -> dict[str, Any]:
    """Promote a schematic only after native KiCad ERC and optional netlist export.

    A baseline KiCad JSON ERC report can be supplied for legacy sources.  In
    that case only newly introduced ERC errors block promotion; without a
    baseline, any native ERC error blocks it.  Warnings remain visible but do
    not block promotion.
    """
    source, document = _schematic_document(path)
    destination = scope.resolve(target) if target else source
    baseline = None
    if baseline_erc is not None:
        baseline_path = scope.resolve(baseline_erc, must_exist=True)
        try:
            baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise BridgeError(f"Invalid baseline ERC JSON {baseline_path}: {exc}") from exc
    netlist = scope.resolve(netlist_output) if netlist_output else None
    result = document.save_and_native_validate(
        destination,
        cli,
        baseline=baseline,
        export_netlist=netlist,
        timeout=timeout,
    )
    schematic_documents[str(destination)] = document
    if destination != source:
        schematic_documents.pop(str(source), None)
    return result


@mcp.tool()
@_tool_error
def kicad_sch_add_symbol(
    path: str,
    lib_id: str,
    reference: Optional[str] = None,
    value: str = "",
    x_mm: float = 100.33,
    y_mm: float = 100.33,
    footprint: Optional[str] = None,
    unit: int = 1,
) -> dict[str, Any]:
    """Add a library-backed symbol; pin mapping remains owned by KiCad libraries."""
    document = _schematic_document(path)[1]
    component = schematic_backend.add_symbol(
        document,
        lib_id=lib_id,
        reference=reference,
        value=value,
        position=(x_mm, y_mm),
        footprint=footprint,
        unit=unit,
    )
    return {"reference": component.reference, "lib_id": component.lib_id, "pins": component.list_pins()}


@mcp.tool()
@_tool_error
def kicad_sch_remove_symbol(path: str, reference: str) -> dict[str, Any]:
    """Remove a symbol by reference from the in-memory schematic."""
    removed = schematic_backend.remove_symbol(_schematic_document(path)[1], reference)
    return {"reference": reference, "removed": removed}


@mcp.tool()
@_tool_error
def kicad_sch_set_symbol_property(path: str, reference: str, name: str, value: str) -> dict[str, Any]:
    """Set one symbol property without editing schematic S-expressions directly."""
    document = _schematic_document(path)[1]
    schematic_backend.set_symbol_property(document, reference, name, value)
    return {"reference": reference, "property": name, "value": value}


@mcp.tool()
@_tool_error
def kicad_sch_set_footprint(path: str, reference: str, footprint: str) -> dict[str, Any]:
    """Assign a footprint property to a schematic symbol."""
    document = _schematic_document(path)[1]
    schematic_backend.set_footprint(document, reference, footprint)
    return {"reference": reference, "footprint": footprint}


@mcp.tool()
@_tool_error
def kicad_sch_get_pins(path: str, reference: str) -> dict[str, Any]:
    """Return library-resolved pin numbers, names, types, and relative positions."""
    return {"reference": reference, "pins": schematic_backend.get_pins(_schematic_document(path)[1], reference)}


@mcp.tool()
@_tool_error
def kicad_sch_connect_pins(path: str, first_reference: str, first_pin: str, second_reference: str, second_pin: str) -> dict[str, Any]:
    """Connect two symbol pins with a backend-generated wire."""
    wire = schematic_backend.connect_pins(
        _schematic_document(path)[1], (first_reference, first_pin), (second_reference, second_pin)
    )
    return {"wire_uuid": wire, "first": [first_reference, first_pin], "second": [second_reference, second_pin]}


@mcp.tool()
@_tool_error
def kicad_sch_add_wire(path: str, start_x_mm: float, start_y_mm: float, end_x_mm: float, end_y_mm: float) -> dict[str, Any]:
    """Add a schematic wire in millimetres."""
    wire = schematic_backend.add_wire(_schematic_document(path)[1], (start_x_mm, start_y_mm), (end_x_mm, end_y_mm))
    return {"wire_uuid": wire}


@mcp.tool()
@_tool_error
def kicad_sch_remove_wire(path: str, wire_uuid: str) -> dict[str, Any]:
    """Remove one wire by UUID from the open schematic."""
    removed = schematic_backend.remove_wire(_schematic_document(path)[1], wire_uuid)
    return {"wire_uuid": wire_uuid, "removed": removed}


@mcp.tool()
@_tool_error
def kicad_sch_add_junction(path: str, x_mm: float, y_mm: float) -> dict[str, Any]:
    """Add an explicit schematic wire junction."""
    uuid = schematic_backend.add_junction(_schematic_document(path)[1], (x_mm, y_mm))
    return {"junction_uuid": uuid, "x_mm": x_mm, "y_mm": y_mm}


@mcp.tool()
@_tool_error
def kicad_sch_move_symbol(path: str, reference: str, x_mm: float, y_mm: float) -> dict[str, Any]:
    """Move a symbol using schematic-library coordinates."""
    schematic_backend.move_symbol(_schematic_document(path)[1], reference, (x_mm, y_mm))
    return {"reference": reference, "x_mm": x_mm, "y_mm": y_mm}


@mcp.tool()
@_tool_error
def kicad_sch_rotate_symbol(path: str, reference: str, rotation: float) -> dict[str, Any]:
    """Rotate a symbol; callers must re-check pin coordinates after rotation."""
    schematic_backend.rotate_symbol(_schematic_document(path)[1], reference, rotation)
    return {"reference": reference, "rotation": rotation}


@mcp.tool()
@_tool_error
def kicad_sch_get_pin_position(path: str, reference: str, pin: str) -> dict[str, Any]:
    """Return one resolved pin position."""
    point = schematic_backend.get_pin_position(_schematic_document(path)[1], reference, pin)
    return {"reference": reference, "pin": pin, "position": {"x": point.x, "y": point.y}}


@mcp.tool()
@_tool_error
def kicad_sch_add_label(path: str, text: str, x_mm: float, y_mm: float, hierarchical: bool = False) -> dict[str, Any]:
    """Add a local or hierarchical label at a specified schematic coordinate."""
    document = _schematic_document(path)[1]
    if hierarchical:
        label_uuid = schematic_backend.add_hierarchical_label(document, text, (x_mm, y_mm))
    else:
        label_uuid = schematic_backend.add_label(document, text, (x_mm, y_mm))
    return {"label_uuid": label_uuid, "text": text, "hierarchical": hierarchical}


@mcp.tool()
@_tool_error
def kicad_sch_add_global_label(path: str, text: str, x_mm: float, y_mm: float, shape: str = "input") -> dict[str, Any]:
    """Add a global label through the schematic backend."""
    label_uuid = schematic_backend.add_global_label(_schematic_document(path)[1], text, (x_mm, y_mm), shape=shape)
    return {"label_uuid": label_uuid, "text": text, "shape": shape}


@mcp.tool()
@_tool_error
def kicad_sch_add_power_symbol(path: str, lib_id: str, reference: str, x_mm: float, y_mm: float) -> dict[str, Any]:
    """Add a library-backed power symbol using the same symbol path as ordinary components."""
    document = _schematic_document(path)[1]
    component = schematic_backend.add_symbol(
        document, lib_id=lib_id, reference=reference, value=lib_id.rsplit(":", 1)[-1], position=(x_mm, y_mm)
    )
    return {"reference": component.reference, "lib_id": component.lib_id}


@mcp.tool()
@_tool_error
def kicad_sch_add_no_connect(path: str, x_mm: float, y_mm: float) -> dict[str, Any]:
    """Add a no-connect marker at a schematic coordinate."""
    marker = schematic_backend.add_no_connect(_schematic_document(path)[1], (x_mm, y_mm))
    return {"uuid": marker.uuid, "x_mm": x_mm, "y_mm": y_mm}


@mcp.tool()
@_tool_error
def kicad_sch_remove_no_connect(path: str, marker_uuid: str) -> dict[str, Any]:
    """Remove one no-connect marker by UUID."""
    removed = schematic_backend.remove_no_connect(_schematic_document(path)[1], marker_uuid)
    return {"uuid": marker_uuid, "removed": removed}


@mcp.tool()
@_tool_error
def kicad_sch_trace_net(path: str, reference: str, pin: str) -> dict[str, Any]:
    """Trace direct-library connectivity from a symbol pin."""
    return {"reference": reference, "pin": pin, "connected_pins": schematic_backend.trace_net(_schematic_document(path)[1], reference, pin)}


@mcp.tool()
@_tool_error
def kicad_sch_add_sheet(
    path: str,
    name: str,
    filename: str,
    x_mm: float,
    y_mm: float,
    width_mm: float = 50.8,
    height_mm: float = 38.1,
) -> dict[str, Any]:
    """Add a hierarchical sheet declaration to an open root schematic."""
    sheet_uuid = schematic_backend.add_sheet(
        _schematic_document(path)[1],
        name=name,
        filename=filename,
        position=(x_mm, y_mm),
        size=(width_mm, height_mm),
    )
    return {"sheet_uuid": sheet_uuid, "name": name, "filename": filename}


@mcp.tool()
@_tool_error
def kicad_sch_add_sheet_pin(
    path: str,
    sheet_uuid: str,
    name: str,
    pin_type: str,
    edge: str,
    position_along_edge_mm: float,
) -> dict[str, Any]:
    """Add a typed hierarchical pin to a sheet declaration."""
    pin_uuid = schematic_backend.add_sheet_pin(
        _schematic_document(path)[1],
        sheet_uuid=sheet_uuid,
        name=name,
        pin_type=pin_type,
        edge=edge,
        position_along_edge=position_along_edge_mm,
    )
    return {"pin_uuid": pin_uuid, "sheet_uuid": sheet_uuid, "name": name}


@mcp.tool()
@_tool_error
def kicad_sch_remove_sheet(path: str, sheet_uuid: str) -> dict[str, Any]:
    """Remove a hierarchical sheet declaration by UUID."""
    removed = schematic_backend.remove_sheet(_schematic_document(path)[1], sheet_uuid)
    return {"sheet_uuid": sheet_uuid, "removed": removed}


@mcp.tool()
@_tool_error
def kicad_sch_list_nets(path: str) -> dict[str, Any]:
    """Return direct-library net records for an open schematic."""
    nets = schematic_backend.list_nets(_schematic_document(path)[1])
    records = []
    for net in nets:
        to_dict = getattr(net, "to_dict", None)
        records.append(to_dict() if callable(to_dict) else {"name": getattr(net, "name", str(net))})
    return {"nets": records}


@mcp.tool()
@_tool_error
def kicad_sch_list_sheets(path: str) -> dict[str, Any]:
    """List hierarchical sheet declarations and pins."""
    return {"sheets": schematic_backend.list_sheets(_schematic_document(path)[1])}


@mcp.tool()
@_tool_error
def kicad_sch_validate_hierarchy(path: str) -> dict[str, Any]:
    """Validate sheet references and hierarchical pin connectivity."""
    return schematic_backend.validate_hierarchy(_schematic_document(path)[1])


@mcp.tool()
@_tool_error
def kicad_sch_find_unconnected_pins(path: str) -> dict[str, Any]:
    """Return library-level connectivity summary for follow-up native ERC."""
    return schematic_backend.find_unconnected_pins(_schematic_document(path)[1])


@mcp.tool()
@_tool_error
def kicad_sch_connectivity_report(path: str) -> dict[str, Any]:
    """Return deterministic structural/connectivity statistics."""
    return schematic_backend.connectivity_report(_schematic_document(path)[1])


@mcp.tool()
@_tool_error
def kicad_sch_search_symbols(pattern: str) -> dict[str, Any]:
    """Search installed and registered project-local symbol libraries."""
    return {"pattern": pattern, "symbols": schematic_backend.search_symbols(pattern)}


@mcp.tool()
@_tool_error
def kicad_sch_get_symbol(lib_id: str) -> dict[str, Any]:
    """Inspect a symbol definition without inferring pin mappings."""
    return {"lib_id": lib_id, "symbol": schematic_backend.get_symbol(lib_id)}


def _board() -> Any:
    return session.board()


def _find_footprint(board: Any, reference_or_id: str) -> FootprintInstance:
    for footprint in board.get_footprints():
        if footprint.reference_field.text.value == reference_or_id or item_id(footprint) == reference_or_id:
            return footprint
    raise BridgeError(f"No footprint found for reference or id {reference_or_id!r}")


@mcp.tool()
@_tool_error
def kicad_board_summary(include_raw: bool = False) -> dict[str, Any]:
    """Inspect the open PCB's file name, item counts, layers, nets, stackup, and title block."""
    def collect(_kicad):
        board = _board()
        collections = ["footprints", "pads", "tracks", "vias", "zones", "graphics", "text", "dimensions", "barcodes", "reference_images", "groups"]
        counts = {kind: len(_board_items(board, kind)) for kind in collections}
        result = {
            "name": board.name,
            "document": jsonable(board.document),
            "counts": counts,
            "copper_layer_count": board.get_copper_layer_count(),
            "enabled_layers": [enum_name(BoardLayer, layer) for layer in board.get_enabled_layers()],
            "nets": [{"name": net.name, "code": int(net.proto.code.value)} for net in board.get_nets()],
            "title_block": jsonable(board.get_title_block_info()),
        }
        if include_raw:
            result["board_sexpr"] = board.get_as_string()
        return result

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_board_dimensions() -> dict[str, Any]:
    """Return KiCad-calculated bounding boxes for board items and a merged content extent."""
    def collect(_kicad):
        board = _board()
        all_items = []
        for kind in ("footprints", "tracks", "vias", "zones", "graphics", "text", "dimensions", "barcodes", "reference_images"):
            all_items.extend(_board_items(board, kind))
        boxes = []
        for item in all_items:
            try:
                box = board.get_item_bounding_box(item, include_text=True)
                if box is not None:
                    boxes.append(jsonable(box))
            except Exception:
                continue
        return {"item_count": len(all_items), "boxes": boxes, "note": "Extent is computed from all returned board items; an empty board has no content extent."}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_board_layers() -> dict[str, Any]:
    """Return enabled, visible, active, and named PCB layers."""
    def collect(_kicad):
        board = _board()
        enabled = board.get_enabled_layers()
        visible = board.get_visible_layers()
        return {
            "enabled": [{"id": layer, "name": enum_name(BoardLayer, layer), "user_name": board.get_layer_name(layer)} for layer in enabled],
            "visible": [{"id": layer, "name": enum_name(BoardLayer, layer)} for layer in visible],
            "active": {"id": board.get_active_layer(), "name": enum_name(BoardLayer, board.get_active_layer())},
            "copper_layer_count": board.get_copper_layer_count(),
        }

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_board_stackup() -> dict[str, Any]:
    """Return the live board stackup."""
    return {"stackup": jsonable(session.call(lambda _kicad: _board().get_stackup()))}


@mcp.tool()
@_tool_error
def kicad_board_design_rules(custom: bool = False) -> dict[str, Any]:
    """Inspect base or custom board design rules."""
    def collect(_kicad):
        board = _board()
        return {"rules": jsonable(board.get_custom_design_rules() if custom else board.get_design_rules()), "custom": custom}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_board_net_classes() -> dict[str, Any]:
    """Inspect project net classes associated with the open PCB."""
    def collect(_kicad):
        project = _board().get_project()
        return {"project": {"name": project.name, "path": project.path}, "net_classes": [jsonable(item) for item in project.get_net_classes()]}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_set_net_classes(net_classes: list[dict[str, Any]], merge_mode: str = "MMM_REPLACE") -> dict[str, Any]:
    """Set project net classes through the supported protobuf command."""
    def collect(_kicad):
        from kipy.proto.common.types import project_settings_pb2
        command = project_commands_pb2.SetNetClasses()
        for value in net_classes:
            parsed = project_settings_pb2.NetClass()
            from google.protobuf.json_format import ParseDict
            ParseDict(value, parsed)
            command.net_classes.append(parsed)
        command.merge_mode = enum_value(MapMergeMode, merge_mode)
        response = session.raw_call(command, Empty)
        return {"updated": True, "response": jsonable(response), "net_classes": net_classes, "merge_mode": merge_mode}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_list_nets(netclass_filter: Optional[str] = None) -> dict[str, Any]:
    """List board nets, optionally filtered by net class."""
    def collect(_kicad):
        board = _board()
        nets = board.get_nets(netclass_filter=netclass_filter) if netclass_filter else board.get_nets()
        return {"nets": [{"name": net.name, "code": int(net.proto.code.value)} for net in nets], "netclass_filter": netclass_filter}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_inspect_net(net_name: str) -> dict[str, Any]:
    """Inspect one net's class and connected PCB items."""
    def collect(_kicad):
        board = _board()
        net = Net(name=net_name)
        items = board.get_items_by_net(net)
        classes = board.get_netclass_for_nets(net)
        return {"net": net_name, "net_classes": {key: jsonable(value) for key, value in classes.items()}, "items": [item_summary(item) for item in items]}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_list_items(kind: str, limit: int = 200, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List a PCB item collection: footprints, pads, tracks, vias, zones, graphics, text, dimensions, barcodes, images, or groups."""
    if limit < 0 or offset < 0:
        raise BridgeError("limit and offset must be non-negative")
    def collect(_kicad):
        items = list(_board_items(_board(), kind))
        return {"kind": kind, "total": len(items), "items": [item_summary(item, include_raw) for item in items[offset:offset + limit]]}

    return session.call(collect)


def _list_alias(kind: str, limit: int, offset: int, include_raw: bool) -> dict[str, Any]:
    return kicad_list_items(kind=kind, limit=limit, offset=offset, include_raw=include_raw)


@mcp.tool()
@_tool_error
def kicad_list_footprints(limit: int = 200, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List PCB footprint instances."""
    return _list_alias("footprints", limit, offset, include_raw)


@mcp.tool()
@_tool_error
def kicad_list_pads(limit: int = 500, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List PCB pads, including pad numbers and padstack data."""
    return _list_alias("pads", limit, offset, include_raw)


@mcp.tool()
@_tool_error
def kicad_list_tracks(limit: int = 500, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List straight and arc copper tracks."""
    return _list_alias("tracks", limit, offset, include_raw)


@mcp.tool()
@_tool_error
def kicad_list_vias(limit: int = 500, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List PCB vias."""
    return _list_alias("vias", limit, offset, include_raw)


@mcp.tool()
@_tool_error
def kicad_list_zones(limit: int = 200, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List PCB copper, rule, and graphic zones."""
    return _list_alias("zones", limit, offset, include_raw)


@mcp.tool()
@_tool_error
def kicad_list_graphics(limit: int = 500, offset: int = 0, include_raw: bool = False) -> dict[str, Any]:
    """List PCB graphic shapes."""
    return _list_alias("graphics", limit, offset, include_raw)


def _inspect_alias(item_id_value: str, expected_kind: str) -> dict[str, Any]:
    result = kicad_inspect_item(item_id_value, include_raw=True)
    actual = result.get("type")
    expected = {
        "footprint": "FootprintInstance",
        "pad": "Pad",
        "track": "Track",
        "via": "Via",
        "zone": "Zone",
        "graphic": {"BoardSegment", "BoardArc", "BoardCircle", "BoardRectangle", "BoardPolygon", "BoardBezier"},
    }[expected_kind]
    if actual != expected and not (isinstance(expected, set) and actual in expected):
        raise BridgeError(f"Item {item_id_value} is {actual}, not a {expected_kind}")
    return result


@mcp.tool()
@_tool_error
def kicad_inspect_footprint(item_id_value: str) -> dict[str, Any]:
    """Inspect one footprint instance by UUID."""
    return _inspect_alias(item_id_value, "footprint")


@mcp.tool()
@_tool_error
def kicad_inspect_pad(item_id_value: str) -> dict[str, Any]:
    """Inspect one pad by UUID."""
    return _inspect_alias(item_id_value, "pad")


@mcp.tool()
@_tool_error
def kicad_inspect_track(item_id_value: str) -> dict[str, Any]:
    """Inspect one track by UUID."""
    return _inspect_alias(item_id_value, "track")


@mcp.tool()
@_tool_error
def kicad_inspect_via(item_id_value: str) -> dict[str, Any]:
    """Inspect one via by UUID."""
    return _inspect_alias(item_id_value, "via")


@mcp.tool()
@_tool_error
def kicad_inspect_zone(item_id_value: str) -> dict[str, Any]:
    """Inspect one zone by UUID."""
    return _inspect_alias(item_id_value, "zone")


@mcp.tool()
@_tool_error
def kicad_inspect_graphic(item_id_value: str) -> dict[str, Any]:
    """Inspect one board graphic by UUID."""
    return _inspect_alias(item_id_value, "graphic")


@mcp.tool()
@_tool_error
def kicad_inspect_item(item_id_value: str, include_raw: bool = True) -> dict[str, Any]:
    """Inspect one PCB object by its KiCad internal UUID."""
    def collect(_kicad):
        items = _board().get_items_by_id(_kiid(item_id_value))
        if not items:
            raise BridgeError(f"No PCB item found with id {item_id_value}")
        return item_summary(items[0], include_raw)

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_query_items_by_region(x_mm: float, y_mm: float, width_mm: float, height_mm: float, kinds: Optional[list[str]] = None) -> dict[str, Any]:
    """Find PCB items whose KiCad-calculated bounding boxes intersect a region in millimeters."""
    if width_mm < 0 or height_mm < 0:
        raise BridgeError("width_mm and height_mm must be non-negative")
    selected = kinds or ["footprints", "pads", "tracks", "vias", "zones", "graphics", "text", "dimensions"]
    def collect(_kicad):
        board = _board()
        left, top = from_mm(x_mm), from_mm(y_mm)
        right, bottom = from_mm(x_mm + width_mm), from_mm(y_mm + height_mm)
        matches = []
        for kind in selected:
            for item in _board_items(board, kind):
                try:
                    box = board.get_item_bounding_box(item, include_text=True)
                    if box is None:
                        continue
                    pos = box.pos
                    size = box.size
                    if pos.x <= right and pos.x + size.x >= left and pos.y <= bottom and pos.y + size.y >= top:
                        matches.append({"kind": kind, "item": item_summary(item)})
                except Exception:
                    continue
        return {"region_mm": {"x": x_mm, "y": y_mm, "width": width_mm, "height": height_mm}, "matches": matches}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_add_footprint(reference: str, value: str = "Codex_Custom", x_mm: float = 50.0, y_mm: float = 50.0, pad_count: int = 2, pad_pitch_mm: float = 2.54, commit_message: str = "Codex add footprint") -> dict[str, Any]:
    """Create a small native PCB footprint with pads through the official IPC create-items path."""
    def collect(_kicad):
        board = _board()
        footprint = _new_footprint(reference, value, x_mm, y_mm, pad_count, pad_pitch_mm)
        commit = board.begin_commit()
        try:
            created = board.create_items(footprint)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"created": [item_summary(item, True) for item in created], "reference": reference, "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_move_footprint(reference: str, x_mm: float, y_mm: float, rotation_deg: Optional[float] = None, commit_message: str = "Codex move footprint") -> dict[str, Any]:
    """Move and optionally rotate an existing footprint using one native undo transaction."""
    def collect(_kicad):
        board = _board()
        fp = _find_footprint(board, reference)
        fp.position = Vector2.from_xy_mm(x_mm, y_mm)
        if rotation_deg is not None:
            fp.orientation = Angle.from_degrees(rotation_deg)
        commit = board.begin_commit()
        try:
            updated = board.update_items(fp)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"updated": [item_summary(item, True) for item in updated], "reference": reference, "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_rotate_footprint(reference: str, rotation_deg: float, commit_message: str = "Codex rotate footprint") -> dict[str, Any]:
    """Rotate an existing footprint around its own origin through the native board model."""
    board = _board()
    fp = _find_footprint(board, reference)
    return kicad_move_footprint(reference, fp.position.x / 1_000_000, fp.position.y / 1_000_000, rotation_deg, commit_message)


@mcp.tool()
@_tool_error
def kicad_modify_footprint(
    reference: str,
    new_reference: Optional[str] = None,
    value: Optional[str] = None,
    layer: Optional[str] = None,
    locked: Optional[bool] = None,
    commit_message: str = "Codex modify footprint",
) -> dict[str, Any]:
    """Modify supported footprint instance properties in one native undo transaction."""
    def collect(_kicad):
        board = _board()
        fp = _find_footprint(board, reference)
        if new_reference is not None:
            fp.reference_field.text.value = new_reference
        if value is not None:
            fp.value_field.text.value = value
        if layer is not None:
            fp.layer = enum_value(BoardLayer, layer)
        if locked is not None:
            fp.locked = locked
        commit = board.begin_commit()
        try:
            updated = board.update_items(fp)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"updated": [item_summary(item, True) for item in updated], "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_delete_footprint(reference: str, commit_message: str = "Codex delete footprint") -> dict[str, Any]:
    """Delete a footprint instance and its contained items in one native undo transaction."""
    def collect(_kicad):
        board = _board()
        fp = _find_footprint(board, reference)
        commit = board.begin_commit()
        try:
            board.remove_items_by_id(_kiid(item_id(fp) or ""))
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"deleted_id": item_id(fp), "reference": reference, "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_add_board_text(value: str, x_mm: float = 50.0, y_mm: float = 50.0, layer: str = "BL_F_SilkS", size_mm: float = 1.0, thickness_mm: float = 0.15, commit_message: str = "Codex add board text") -> dict[str, Any]:
    """Add native board text in one KiCad undo transaction."""
    def collect(_kicad):
        board = _board()
        text = _new_text(value, x_mm, y_mm, layer, size_mm, thickness_mm)
        commit = board.begin_commit()
        try:
            created = board.create_items(text)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"created": [item_summary(item, True) for item in created], "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_add_graphic(
    shape: str,
    layer: str = "BL_Edge_Cuts",
    start_x_mm: float = 0.0,
    start_y_mm: float = 0.0,
    end_x_mm: float = 10.0,
    end_y_mm: float = 10.0,
    width_mm: float = 0.05,
    commit_message: str = "Codex add graphic",
) -> dict[str, Any]:
    """Add a native PCB segment, rectangle, or circle graphic."""
    normalized = shape.lower().replace("-", "_")
    classes = {"segment": BoardSegment, "line": BoardSegment, "rectangle": BoardRectangle, "circle": BoardCircle}
    if normalized not in classes:
        raise BridgeError("shape must be one of: segment, line, rectangle, circle")

    def collect(_kicad):
        board = _board()
        graphic = classes[normalized]()
        graphic.layer = enum_value(BoardLayer, layer)
        attributes = GraphicAttributes()
        attributes.stroke.width = from_mm(width_mm)
        graphic.attributes = attributes
        if isinstance(graphic, BoardSegment):
            graphic.start = Vector2.from_xy_mm(start_x_mm, start_y_mm)
            graphic.end = Vector2.from_xy_mm(end_x_mm, end_y_mm)
        elif isinstance(graphic, BoardRectangle):
            graphic.top_left = Vector2.from_xy_mm(start_x_mm, start_y_mm)
            graphic.bottom_right = Vector2.from_xy_mm(end_x_mm, end_y_mm)
        else:
            graphic.center = Vector2.from_xy_mm(start_x_mm, start_y_mm)
            graphic.radius_point = Vector2.from_xy_mm(end_x_mm, end_y_mm)
        commit = board.begin_commit()
        try:
            created = board.create_items(graphic)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"created": [item_summary(item, True) for item in created], "shape": normalized, "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_create_track(start_x_mm: float, start_y_mm: float, end_x_mm: float, end_y_mm: float, layer: str = "BL_F_Cu", width_mm: float = 0.25, net_name: str = "", commit_message: str = "Codex create track") -> dict[str, Any]:
    """Create a native straight copper track segment."""
    def collect(_kicad):
        board = _board()
        track = Track()
        track.start = Vector2.from_xy_mm(start_x_mm, start_y_mm)
        track.end = Vector2.from_xy_mm(end_x_mm, end_y_mm)
        track.layer = enum_value(BoardLayer, layer)
        track.width = from_mm(width_mm)
        if net_name:
            track.net = Net(name=net_name)
        commit = board.begin_commit()
        try:
            created = board.create_items(track)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"created": [item_summary(item, True) for item in created], "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_create_via(x_mm: float, y_mm: float, diameter_mm: float = 0.8, drill_mm: float = 0.4, net_name: str = "", commit_message: str = "Codex create via") -> dict[str, Any]:
    """Create a native through via."""
    def collect(_kicad):
        board = _board()
        via = Via()
        via.position = Vector2.from_xy_mm(x_mm, y_mm)
        via.type = ViaType.VT_THROUGH
        via.diameter = from_mm(diameter_mm)
        via.drill_diameter = from_mm(drill_mm)
        if net_name:
            via.net = Net(name=net_name)
        commit = board.begin_commit()
        try:
            created = board.create_items(via)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"created": [item_summary(item, True) for item in created], "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_update_board_text(item_id_value: str, value: Optional[str] = None, x_mm: Optional[float] = None, y_mm: Optional[float] = None, layer: Optional[str] = None, commit_message: str = "Codex update board text") -> dict[str, Any]:
    """Update native board text properties using one undo transaction."""
    def collect(_kicad):
        board = _board()
        items = board.get_items_by_id(_kiid(item_id_value))
        if not items or not isinstance(items[0], BoardText):
            raise BridgeError(f"Item {item_id_value} is not a board text item")
        text = items[0]
        if value is not None:
            text.value = value
        if x_mm is not None and y_mm is not None:
            text.position = Vector2.from_xy_mm(x_mm, y_mm)
        elif x_mm is not None or y_mm is not None:
            raise BridgeError("x_mm and y_mm must be supplied together")
        if layer is not None:
            text.layer = enum_value(BoardLayer, layer)
        commit = board.begin_commit()
        try:
            updated = board.update_items(text)
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"updated": [item_summary(item, True) for item in updated], "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_delete_items(item_ids: list[str], commit_message: str = "Codex delete board items") -> dict[str, Any]:
    """Delete PCB objects by KiCad UUID in one native undo transaction."""
    if not item_ids:
        raise BridgeError("item_ids must not be empty")
    def collect(_kicad):
        board = _board()
        commit = board.begin_commit()
        try:
            board.remove_items_by_id([_kiid(value) for value in item_ids])
            board.push_commit(commit, commit_message)
        except Exception:
            board.drop_commit(commit)
            raise
        return {"deleted_ids": item_ids, "commit_message": commit_message}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_get_selection() -> dict[str, Any]:
    """Read the current PCB editor selection."""
    return {"selection": [item_summary(item, True) for item in session.call(lambda _kicad: _board().get_selection())]}


@mcp.tool()
@_tool_error
def kicad_set_selection(item_ids: list[str]) -> dict[str, Any]:
    """Replace PCB selection with the supplied item UUIDs."""
    def collect(_kicad):
        board = _board()
        board.clear_selection()
        items = board.get_items_by_id([_kiid(value) for value in item_ids]) if item_ids else []
        selected = board.add_to_selection(items) if items else []
        return {"selection": [item_summary(item, True) for item in selected]}

    return session.call(collect)


@mcp.tool()
@_tool_error
def kicad_run_action(action: str) -> dict[str, Any]:
    """Invoke KiCad's documented IPC action escape hatch; action names are KiCad-version-specific and unstable."""
    return {"action": action, "response": jsonable(session.call(lambda k: k.run_action(action)))}


@mcp.tool()
@_tool_error
def kicad_save() -> dict[str, Any]:
    """Save the open PCB through KiCad IPC."""
    session.call(lambda _kicad: _board().save())
    return {"saved": True, "document": "open PCB"}


@mcp.tool()
@_tool_error
def kicad_save_as(path: str, overwrite: bool = False, include_project: bool = True) -> dict[str, Any]:
    """Save the open PCB to a scoped path through KiCad IPC."""
    target = scope.resolve(path)
    session.call(lambda _kicad: _board().save_as(str(target), overwrite=overwrite, include_project=include_project))
    return {"saved_as": str(target), "overwrite": overwrite, "include_project": include_project}


@mcp.tool()
@_tool_error
def kicad_reload() -> dict[str, Any]:
    """Revert the open PCB to its last saved state through KiCad IPC."""
    session.call(lambda _kicad: _board().revert())
    return {"reloaded": True, "document": "open PCB"}


@mcp.tool()
@_tool_error
def kicad_drc(input_file: str, output_file: Optional[str] = None, report_format: str = "json", extra_args: Optional[list[str]] = None, timeout: int = 120) -> dict[str, Any]:
    """Run KiCad 10 PCB DRC and return the machine-readable report when JSON is requested."""
    input_path = scope.resolve(input_file, must_exist=True)
    output_path = scope.resolve(output_file) if output_file else None
    return cli.validate("drc", input_path, output_path, report_format, extra_args, timeout)


@mcp.tool()
@_tool_error
def kicad_erc(input_file: str, output_file: Optional[str] = None, report_format: str = "json", extra_args: Optional[list[str]] = None, timeout: int = 120) -> dict[str, Any]:
    """Run KiCad 10 schematic ERC and return the machine-readable report when JSON is requested."""
    input_path = scope.resolve(input_file, must_exist=True)
    output_path = scope.resolve(output_file) if output_file else None
    return cli.validate("erc", input_path, output_path, report_format, extra_args, timeout)


@mcp.tool()
@_tool_error
def kicad_unrouted_items(input_file: str, output_file: Optional[str] = None) -> dict[str, Any]:
    """Run JSON DRC and return unconnected/unrouted violations separately."""
    result = kicad_drc(input_file, output_file, "json")
    report = result.get("report")
    violations = report.get("violations", []) if isinstance(report, dict) else []
    unrouted = [item for item in violations if "unconnected" in json.dumps(item).lower() or "unrouted" in json.dumps(item).lower()]
    return {"drc": result, "unrouted_items": unrouted, "count": len(unrouted)}


@mcp.tool()
@_tool_error
def kicad_cli_capabilities(subcommand: Optional[str] = None) -> dict[str, Any]:
    """Return the installed kicad-cli help surface."""
    args = [] if not subcommand else subcommand.split()
    return {"version": cli.version(), "help": cli.help(args)}


@mcp.tool()
@_tool_error
def kicad_cli_export(operation: str, input_file: str, output: str, extra_args: Optional[list[str]] = None, timeout: int = 180) -> dict[str, Any]:
    """Run a structured KiCad 10 export operation without invoking a shell."""
    input_path = scope.resolve(input_file, must_exist=True)
    output_path = scope.resolve(output)
    return cli.export(operation, input_path, output_path, extra_args, timeout)


@mcp.tool()
@_tool_error
def kicad_list_project_files(path: str = ".", max_entries: int = 1000) -> dict[str, Any]:
    """List KiCad source, library, configuration, and generated files under the scoped project root."""
    target = scope.resolve(path, must_exist=True)
    if not target.is_dir():
        raise BridgeError(f"Not a directory: {target}")
    paths = []
    for candidate in sorted(target.rglob("*")):
        if candidate.is_file():
            paths.append(str(candidate.relative_to(scope.root)))
            if len(paths) >= max_entries:
                break
    return {"root": str(scope.root), "path": str(target), "entries": paths, "truncated": len(paths) >= max_entries}


@mcp.tool()
@_tool_error
def kicad_read_project_file(path: str, max_bytes: int = 10_000_000) -> dict[str, Any]:
    """Read a scoped KiCad source/config/generated file as UTF-8 text or base64 for binary data."""
    target = scope.resolve(path, must_exist=True)
    if target.stat().st_size > max_bytes:
        raise BridgeError(f"File is larger than max_bytes={max_bytes}: {target}")
    data = target.read_bytes()
    try:
        content = data.decode("utf-8")
        encoding = "utf-8"
    except UnicodeDecodeError:
        content = base64.b64encode(data).decode("ascii")
        encoding = "base64"
    return {"path": str(target), "bytes": len(data), "encoding": encoding, "content": content}


@mcp.tool()
@_tool_error
def kicad_write_project_file(path: str, content: str, encoding: str = "utf-8") -> dict[str, Any]:
    """Atomically write a scoped KiCad source/config/generated file; validate it separately with kicad_drc/kicad_erc."""
    if encoding not in {"utf-8", "base64"}:
        raise BridgeError("encoding must be 'utf-8' or 'base64'")
    payload = base64.b64decode(content) if encoding == "base64" else content
    if isinstance(payload, bytes):
        target = scope.resolve(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        temp = target.with_name(f".{target.name}.{uuid.uuid4().hex}.tmp")
        temp.write_bytes(payload)
        os.replace(temp, target)
        return {"path": str(target), "bytes": len(payload), "encoding": encoding}
    return scope.write(path, payload, encoding="utf-8")


@mcp.tool()
@_tool_error
def kicad_validate_file(path: str, output_file: Optional[str] = None, timeout: int = 120) -> dict[str, Any]:
    """Validate a .kicad_pcb with DRC or .kicad_sch with ERC using KiCad itself."""
    target = scope.resolve(path, must_exist=True)
    if target.suffix.lower() == ".kicad_pcb":
        return kicad_drc(path, output_file, "json", timeout=timeout)
    if target.suffix.lower() == ".kicad_sch":
        return kicad_erc(path, output_file, "json", timeout=timeout)
    raise BridgeError("KiCad CLI validation supports .kicad_pcb (DRC) and .kicad_sch (ERC)")


@mcp.tool()
@_tool_error
def kicad_list_api(prefix: str = "") -> dict[str, Any]:
    """List protobuf message/enum definitions shipped by the installed official kicad-python binding."""
    return registry.list_api(prefix)


@mcp.tool()
@_tool_error
def kicad_describe_object(object_type: str) -> dict[str, Any]:
    """Describe a protobuf object type, its fields, nested messages, and enum choices."""
    return registry.describe(object_type)


@mcp.tool()
@_tool_error
def kicad_describe_method(request_type: str, response_type: Optional[str] = None) -> dict[str, Any]:
    """Describe an IPC request and response message; response is inferred by KiCad naming convention when omitted."""
    return registry.describe_method(request_type, response_type)


def _set_nested_value(document: dict[str, Any], path: str, value: Any) -> dict[str, Any]:
    parts = path.split(".")
    cursor = document
    for part in parts[:-1]:
        current = cursor.get(part)
        if not isinstance(current, dict):
            current = {}
            cursor[part] = current
        cursor = current
    cursor[parts[-1]] = value
    return document


@mcp.tool()
@_tool_error
def kicad_get_property(message_type: str, property_path: str, message: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    """Inspect a protobuf property descriptor and optionally read that property from a JSON message."""
    description = registry.describe(message_type)
    current: Any = message
    for part in property_path.split("."):
        if not isinstance(current, dict) or part not in current:
            current = None
            break
        current = current[part]
    return {"message_type": description["full_name"], "property_path": property_path, "value": current, "message_schema": description}


@mcp.tool()
@_tool_error
def kicad_set_property(message_type: str, property_path: str, value: Any, message: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    """Set a protobuf property in a validated JSON message payload without invoking KiCad."""
    base = dict(message or {})
    _set_nested_value(base, property_path, value)
    registry.message(message_type, base)
    return {"message_type": registry.resolve_message(message_type).full_name, "property_path": property_path, "message": base}


@mcp.tool()
@_tool_error
def kicad_raw_call(request_type: str, response_type: Optional[str] = None, arguments: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    """Invoke a normal, descriptor-discovered KiCad IPC protobuf command; no arbitrary memory or shell access is provided."""
    response_name = response_type or _infer_response_type(registry, request_type)
    request = registry.message(request_type, arguments or {})
    response_descriptor = registry.resolve_message(response_name)
    response_class = __import__("google.protobuf.message_factory", fromlist=["GetMessageClass"]).GetMessageClass(response_descriptor)
    response = session.raw_call(request, response_class)
    return {"request_type": registry.resolve_message(request_type).full_name, "response_type": response_descriptor.full_name, "response": jsonable(response)}


if __name__ == "__main__":
    mcp.run()
