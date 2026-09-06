"""Negative control: removing a required JMS583 support part must fail audit."""
from pathlib import Path
import subprocess, tempfile
ROOT=Path(__file__).resolve().parent
src=ROOT/'STORAGE.kicad_sch'; text=src.read_text()
start=text.index('(symbol (lib_id "PiSXMeRevAClean:STORAGE_PASSIVE_2")')
while 'property "Reference" "R80"' not in text[start:start+5000]:
 start=text.index('(symbol (lib_id "PiSXMeRevAClean:STORAGE_PASSIVE_2")',start+1)
end=start+len(text[start:])
# Remove the complete R34 instance by its reference block boundary.
next_start=text.find('(symbol (lib_id ',start+1)
if next_start < 0: next_start=len(text)
trial=Path(tempfile.mkstemp(suffix='.kicad_sch')[1]); trial.write_text(text[:start]+text[next_start:])
r=subprocess.run(['python3',str(ROOT/'phase24_jms583_support_audit.py'),str(trial)],capture_output=True,text=True)
trial.unlink()
if r.returncode==0: raise SystemExit('FAIL negative control unexpectedly passed')
print('PASS negative control: removed R80 support is rejected')
