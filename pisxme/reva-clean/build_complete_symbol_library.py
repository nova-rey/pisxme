"""Assemble the clean project's external symbol library from embedded authorities."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'PiSXMe_RevA_Clean_complete.kicad_sym'

def block_end(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '(':
            depth += 1
        elif text[i] == ')':
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError(start)

def symbols_from(text):
    out = []
    pos = 0
    while pos < len(text):
        hit = text.find('(symbol "PiSXMeRevAClean:', pos)
        if hit < 0:
            break
        name_end = text.find('"', hit + len('(symbol "'))
        name = text[hit + len('(symbol "'):name_end]
        if name.endswith('_1_1'):
            pos = name_end + 1
            continue
        begin = hit
        end = block_end(text, begin)
        out.append(text[begin:end])
        pos = end
    # Several recovered child sheets carry custom symbol definitions at column
    # zero after lib_symbols.  Normalize those into the clean library namespace.
    import re
    for match in re.finditer(r'(?m)^\(symbol "([A-Za-z0-9_]+)"', text):
        name = match.group(1)
        if name.endswith('_1_1') or ':' in name:
            continue
        end = block_end(text, match.start())
        block = text[match.start():end]
        block = block.replace(f'(symbol "{name}"', f'(symbol "PiSXMeRevAClean:{name}"', 1)
        out.append(block)
    return out

def main():
    files = [ROOT / 'PiSXMe_RevA_Clean.kicad_sch'] + sorted(ROOT.glob('*.kicad_sch'))
    symbols = {}
    for path in files:
        for symbol in symbols_from(path.read_text()):
            name = symbol.split('"', 2)[1]
            symbols.setdefault(name, symbol)
    header = '(kicad_symbol_lib\n\t(version 20231120)\n\t(generator "PiSXMe Rev A Clean")\n'
    OUT.write_text(header + ''.join('\t' + s + '\n' for s in sorted(symbols.values())) + ')\n')
    print(f'{OUT}: {len(symbols)} symbols')

if __name__ == '__main__': main()
