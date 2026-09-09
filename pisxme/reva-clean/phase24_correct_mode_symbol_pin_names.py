"""Reconcile embedded storage symbol pin names with the live mode authority."""
from pathlib import Path
from phase3_scaffold import balanced
from phase24_integrate_dual_mode_storage import definition, M2, USB

ROOT = Path(__file__).resolve().parent
SCH = ROOT / "STORAGE.kicad_sch"

def replace_definition(text, name, pinmap):
    needle = f'(symbol "PiSXMeRevAClean:{name}"'
    start = text.index(needle)
    end = start + len(balanced(text, start))
    return text[:start] + definition(name, pinmap) + text[end:]

text = SCH.read_text()
# Regenerate the embedded definitions, not only instance labels. Native
# netlist export resolves pin ownership from these definitions.
text = replace_definition(text, "HD3SS6126_RUA0042A", USB)
text = replace_definition(text, "TE_1-2199230-4_MKEY", M2)
# The mode buffer's pin 2 is the same reviewed AUTO_PEDET authority as J3.69.
start = text.index('(symbol "PiSXMeRevAClean:STORAGE_MODE_BUFFER"')
end = start + len(balanced(text, start))
block = text[start:end].replace('(name "M2_PEDET"', '(name "AUTO_PEDET"')
text = text[:start] + block + text[end:]
SCH.write_text(text)
print("corrected embedded mode pin names for U12, J3, and mode buffer")
