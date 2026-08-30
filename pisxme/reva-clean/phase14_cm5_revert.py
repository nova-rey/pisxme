"""Remove the rejected single-unit CM5 promotion, restoring the clean sheet."""
from pathlib import Path
import re
from phase3_scaffold import balanced

PATH = Path(__file__).resolve().parent / 'CORE_CM5.kicad_sch'

def remove_expr(text, marker):
    while marker in text:
        start = text.index(marker)
        text = text[:start] + text[start + len(balanced(text, start)):]
    return text

def main():
    text = PATH.read_text()
    text = remove_expr(text, '(symbol "PiSXMeRevAClean:ComputeModule5-CM5"')
    text = remove_expr(text, '(symbol (lib_id "PiSXMeRevAClean:ComputeModule5-CM5")')
    text = re.sub(r'\(label "[^"]+"[^\n]*\(uuid e3000000-0000-0000-0000-[0-9a-f]+\)\)', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    PATH.write_text(text)
    print('Phase 14 CM5 promotion reverted: two-unit native mapping remains open')

if __name__ == '__main__': main()
