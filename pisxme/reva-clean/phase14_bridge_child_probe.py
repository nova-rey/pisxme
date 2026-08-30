"""Round-trip a disposable REGULATORS child through the installed bridge API."""
from pathlib import Path
import shutil
from bridge.schematic_backend import SchematicBackend

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "bridge-child-probe"
OUT.mkdir(exist_ok=True)
src = ROOT / "REGULATORS.kicad_sch"
dst = OUT / "REGULATORS.kicad_sch"
shutil.copy2(src, dst)
backend = SchematicBackend()
doc = backend.open(dst)
doc.schematic.components.add("Device:C", reference="Z99", value="100n", position=(220, 150), footprint="PiSXMeRevAClean:C_0805_2012Metric")
doc.save(dst, validate=False)
print(dst)
