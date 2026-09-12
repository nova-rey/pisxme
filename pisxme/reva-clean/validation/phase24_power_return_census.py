#!/usr/bin/env python3
"""Read-only native PCB object census for Phase 24 power/return evidence.

This intentionally parses the committed KiCad PCB serialization without writing
CAD. Native DRC is run separately by the qualified KiCad Light worker.
"""
from pathlib import Path
import re, json, collections, hashlib, sys

class ParseError(Exception): pass

def toks(s):
    i=0; n=len(s)
    while i<n:
        c=s[i]
        if c.isspace(): i+=1; continue
        if c in '();':
            yield c; i+=1; continue
        if c=='"':
            j=i+1; out=[]
            while j<n:
                if s[j]=='\\' and j+1<n:
                    out.append(s[j+1]); j+=2
                elif s[j]=='"':
                    yield ''.join(out); i=j+1; break
                else: out.append(s[j]); j+=1
            else: raise ParseError('unterminated string')
            continue
        j=i
        while j<n and (not s[j].isspace()) and s[j] not in '();': j+=1
        yield s[i:j]; i=j

def parse(s):
    ts=iter(toks(s))
    def one():
        x=next(ts)
        if x=='(':
            a=[]
            while True:
                x=next(ts)
                if x==')': return a
                if x=='(': # pushback unavailable; parse from a marker
                    a.append(one_after_open())
                else: a.append(x)
        raise ParseError(x)
    def one_after_open():
        a=[]
        while True:
            x=next(ts)
            if x==')': return a
            if x=='(': a.append(one_after_open())
            else:a.append(x)
    return one()

def asfloat(x):
    try:return float(x)
    except:return None

def first(x,k):
    return next((y for y in x[1:] if isinstance(y,list) and y and y[0]==k),None)
def allsub(x,k):
    return [y for y in x[1:] if isinstance(y,list) and y and y[0]==k]
def value(x,k,default=None):
    a=first(x,k); return a[1] if a and len(a)>1 else default

def collect(ref):
    path=Path(ref); txt=path.read_text(); root=parse(txt)
    sha=hashlib.sha256(txt.encode()).hexdigest()
    nets={}; fps=[]; seg=[]; vias=[]; zones=[]
    for x in root[1:]:
        if not isinstance(x,list) or not x: continue
        k=x[0]
        if k=='net' and len(x)>=3: nets[str(x[1])] = str(x[2])
        elif k=='footprint': fps.append(x)
        elif k=='segment': seg.append(x)
        elif k=='via': vias.append(x)
        elif k=='zone': zones.append(x)
    # footprint ref and pads
    power={'12V_PROTECTED','POWER_GND','FUSED_12V_A','FUSED_12V_B','12V_IN_A','12V_IN_B','CM5_5V','BRIDGE_3V3','BRIDGE_1V1','STORAGE_3V3','JMS_AVDD33','JMS_AVDDL','JMS_VCCO','JMS_VDDREG_5V'}
    fpinfo=[]; padcounts=collections.defaultdict(collections.Counter)
    padrefs=collections.defaultdict(list)
    for fp in fps:
        pr=None
        for p in allsub(fp,'property'):
            if len(p)>=3 and p[1]=='Reference': pr=str(p[2]); break
        if not pr: continue
        names=[]
        for p in allsub(fp,'pad'):
            nn=first(p,'net'); netname=str(nn[-1]) if nn and len(nn)>=2 else '<no net>'
            padcounts[netname]['pads']+=1
            if netname in power:
                padrefs[netname].append(f'{pr}.{p[1]}')
        fpinfo.append(pr)
    def item_net(x):
        n=first(x,'net'); return str(n[-1]) if n and len(n)>=2 else '<none>'
    def item_attr(x,k):
        a=first(x,k);return a[1] if a and len(a)>1 else None
    seg_by=collections.Counter(); via_by=collections.Counter(); seg_len=collections.defaultdict(float)
    for x in seg:
        n=item_net(x); seg_by[n]+=1
        a=first(x,'start'); b=first(x,'end')
        if a and b: seg_len[n]+=((float(a[1])-float(b[1]))**2+(float(a[2])-float(b[2]))**2)**0.5
    via_layers=collections.Counter();
    for x in vias:
        n=item_net(x); via_by[n]+=1
        l=first(x,'layers'); via_layers[(n,tuple(l[1:]) if l else ())]+=1
    zone_by=collections.Counter(); zone_layers=collections.defaultdict(list); zone_names=collections.defaultdict(list)
    for x in zones:
        n=item_net(x); layer=item_attr(x,'layer'); zone_by[n]+=1
        zone_layers[n].append(layer); zone_names[n].append(str(value(x,'name','<unnamed>')))
    alln=sorted(power | set(padcounts) | set(seg_by) | set(via_by) | set(zone_by)); out={'board':str(path),'sha256':sha,'nets':{n:{'pads':padcounts[n]['pads'],'segments':seg_by[n],'vias':via_by[n],'segment_length_mm':round(seg_len[n],4),'zones':zone_by[n],'zone_layers':zone_layers[n],'zone_names':zone_names[n], 'sample_pads':padrefs[n][:15]} for n in alln if n in power},'totals':{'footprints':len(fps),'segments':len(seg),'vias':len(vias),'zones':len(zones)}}
    return out

if __name__=='__main__':
 out=collect(sys.argv[1]); print(json.dumps(out,indent=2,sort_keys=True))
