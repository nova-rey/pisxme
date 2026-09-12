"""Disposable probe: replace exact duplicate STORAGE NC labels by named aliases."""
from pathlib import Path
import shutil, subprocess

R = Path(__file__).resolve().parent
OUT = R / ".phase24_storage_duplicate_label_probe_v1"
if OUT.exists():
    raise SystemExit("probe output exists; refusing overwrite")
OUT.mkdir()
children = ["CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
            "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG"]
for name in ["PiSXMe_RevA_Clean.kicad_sch", "PiSXMe_RevA_Clean.kicad_pro",
             "PiSXMe_RevA_Clean_complete.kicad_sym", "Storage_DualMode.kicad_sym",
             "sym-lib-table", "fp-lib-table"] + [x + ".kicad_sch" for x in children]:
    shutil.copy2(R / name, OUT / name)
shutil.copytree(R / "PiSXMe_RevA_Clean.pretty", OUT / "PiSXMe_RevA_Clean.pretty")

mapping = {
    "NC_1": "JMS_VDDREG_5V", "NC_2": "JMS_VCCK", "NC_3": "JMS_SPI_SO_DNP",
    "NC_4": "JMS_SPI_SCK_DNP", "NC_5": "JMS_SPI_SI_DNP", "NC_6": "JMS_VCCO",
    "NC_7": "JMS_SPI_CS_N_DNP", "NC_8": "JMS_GPIO4_NC", "NC_9": "JMS_GPIO5_NC",
    "NC_13": "JMS_GPIO8_NC", "NC_14": "JMS_GPIO9_NC", "NC_15": "JMS_RESET_N",
    "NC_19": "JMS_AVDD33", "NC_20": "JMS_AVDDL", "NC_52": "JMS_XAVDDH",
    "NC_57": "JMS_GPIO12_NC", "NC_58": "JMS_GPIO11_NC", "NC_59": "JMS_GPIO10_NC",
    "NC_61": "JMS_CC2_NC", "NC_62": "JMS_CC1_NC",
}

def records(text):
    i = 0
    while True:
        i = text.find('(label "', i)
        if i < 0:
            return
        j, depth, quote, escaped = i, 0, False, False
        while j < len(text):
            ch = text[j]
            if quote:
                if escaped: escaped = False
                elif ch == "\\": escaped = True
                elif ch == '"': quote = False
            else:
                if ch == '"': quote = True
                elif ch == "(": depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        yield i, j + 1, text[i:j + 1]
                        i = j + 1
                        break
            j += 1

p = OUT / "STORAGE.kicad_sch"
text = p.read_text()
found = []
for start, end, record in records(text):
    name = record.split('"', 2)[1]
    if name in mapping and "(at 70 " in record:
        found.append((start, end, name, mapping[name]))
if len(found) != len(mapping):
    raise SystemExit(f"expected {len(mapping)} exact records, found {len(found)}")
for start, end, old, new in reversed(found):
    text = text[:start] + text[start:end].replace(f'(label "{old}"', f'(label "{new}"', 1) + text[end:]
p.write_text(text)
print("renamed", len(found), "duplicate labels")
kicad = ["kicad-cli"] if shutil.which("kicad-cli") else ["flatpak", "run", "--command=kicad-cli", "org.kicad.KiCad"]
result = subprocess.run(kicad + ["sch", "erc", "--severity-all", "--output", str(OUT / "erc.rpt"),
                                 str(OUT / "PiSXMe_RevA_Clean.kicad_sch")], cwd=OUT, text=True,
                        capture_output=True)
print(result.stdout.strip())
print(result.stderr.strip())
print("erc_rc", result.returncode)
