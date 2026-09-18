#!/usr/bin/env python3
"""Read-only local regulator support census for the exact integrated board."""
from __future__ import annotations
import hashlib, json, math, re, sys
from pathlib import Path

def blocks(text, token):
    needle='('+token; pos=0
    while True:
        start=text.find(needle,pos)
        if start<0: return
        if start and text[start-1] not in '\n\r\t ':
            pos=start+1; continue
        depth=0; quote=False; escaped=False
        for i in range(start,len(text)):
            c=text[i]
            if quote:
                if escaped: escaped=False
                elif c=='\\': escaped=True
                elif c=='"': quote=False
            elif c=='"': quote=True
            elif c=='(': depth+=1
            elif c==')':
                depth-=1
                if depth==0:
                    yield text[start:i+1]; pos=i+1; break
        else: raise ValueError('unbalanced '+token)

def first(p,t,d=None):
    m=re.search(p,t,re.S); return m.group(1) if m else d

def xy(t,atom='at'):
    m=re.search(r'\('+re.escape(atom)+r'\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)',t)
    return [float(m.group(1)),float(m.group(2))] if m else None

def rotxy(p, o, deg):
    a=math.radians(deg); return [o[0]+p[0]*math.cos(a)-p[1]*math.sin(a), o[1]+p[0]*math.sin(a)+p[1]*math.cos(a)]

def pad_data(b,o,deg):
    out=[]
    for p in blocks(b,'pad'):
        num=first(r'^\(pad\s+"([^"]+)"',p)
        local=xy(p)
        if num is None or local is None: continue
        net=first(r'\(net\s+"([^"]*)"',p,'')
        size=first(r'\(size\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)',p)
        drill=first(r'\(drill\s+([-+0-9.eE]+)',p)
        layers=re.findall(r'\(layers\s+([^\)]*)\)',p)
        out.append({'number':num,'net':net,'local_mm':local,'absolute_mm':rotxy(local,o,deg),'size_mm':[float(x) for x in size.split()] if size else None,'drill_mm':float(drill) if drill else None,'layers':layers[0].strip() if layers else None})
    return out

def parse(board):
    text=board.read_text(); fps=[]
    for b in blocks(text,'footprint'):
        o=xy(b)
        if o is None: continue
        ar=re.search(r'\(at\s+[-+0-9.eE]+\s+[-+0-9.eE]+(?:\s+([-+0-9.eE]+))?',b)
        deg=float(ar.group(1) or 0) if ar else 0.0
        ref=first(r'\(property\s+"Reference"\s+"([^"]+)"',b)
        val=first(r'\(property\s+"Value"\s+"([^"]*)"',b,'')
        name=first(r'^\(footprint\s+"([^"]+)"',b,'')
        fps.append({'reference':ref,'value':val,'footprint':name,'origin_mm':o,'rotation_deg':deg,'pads':pad_data(b,o,deg)})
    byref={x['reference']:x for x in fps if x['reference']}
    groups={
      'U3': ['C5','C6','C7','C8','C9','R3','R4','R5','R6'],
      'U4': ['C14','C15','C16','C17','C18','C19','R11','R12','R13','R14'],
      'U5': ['C23','C24','C25','C26','C27','C28','C29','C34','C35','C36','C37','C38','C39','C40','C41','C44','C45','C46','C47','R19','R20','R21','R22'],
    }
    supports={}
    for u, refs in groups.items():
        supports[u]={'regulator':byref.get(u),'cohort':{r:byref.get(r) for r in refs}}
    return {'board':board.name,'board_sha256':hashlib.sha256(board.read_bytes()).hexdigest(),'supports':supports}

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: census_support.py BOARD OUTPUT_JSON')
    Path(sys.argv[2]).write_text(json.dumps(parse(Path(sys.argv[1])),indent=2,sort_keys=True)+'\n')
