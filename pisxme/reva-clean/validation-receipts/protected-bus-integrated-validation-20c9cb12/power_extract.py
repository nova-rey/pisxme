import re,json,math,hashlib,sys
from pathlib import Path
p=Path(sys.argv[1]); s=p.read_text()
# use bounded block regex: each segment/via ends at first tab-close. All fields are simple.
seg_re=re.compile(r'\(segment\s+\(start\s+([0-9.+-]+)\s+([0-9.+-]+)\)\s+\(end\s+([0-9.+-]+)\s+([0-9.+-]+)\)\s+\(width\s+([0-9.+-]+)\)\s+\(layer\s+"([^"]+)"\)\s+\(net\s+"([^"]+)"\)',re.M)
via_re=re.compile(r'\(via\s+\(at\s+([0-9.+-]+)\s+([0-9.+-]+)\)\s+\(size\s+([0-9.+-]+)\)\s+\(drill\s+([0-9.+-]+)\)\s+\(layers\s+"([^"]+)"\s+"([^"]+)"\)\s+\(net\s+"([^"]+)"\)',re.M)
segs=[]
for a,b,c,d,w,l,n in seg_re.findall(s):
 x1,y1,x2,y2,w=map(float,(a,b,c,d,w)); segs.append({'x1':x1,'y1':y1,'x2':x2,'y2':y2,'length_mm':math.hypot(x2-x1,y2-y1),'width_mm':w,'layer':l,'net':n})
vias=[]
for a,b,sz,dr,la,lb,n in via_re.findall(s): vias.append({'x':float(a),'y':float(b),'size_mm':float(sz),'drill_mm':float(dr),'layers':[la,lb],'net':n})
# zone definitions (not filled polys), enough to establish net/layer and count
zone_re=re.compile(r'\(zone\s+\(net\s+"([^"]+)"\)\s+\(layer\s+"([^"]+)"\)',re.M)
zones=[{'net':n,'layer':l} for n,l in zone_re.findall(s)]
target=['12V_IN_A','12V_IN_B','FUSED_12V_A','FUSED_12V_B','12V_PROTECTED','POWER_GND']
# 1oz conservative sheet resistance; do not treat as closure; assumes 35um copper and ignores spreading/contacts.
rho=1.724e-8; thickness=35e-6
out={'source':str(p),'pcb_sha256':hashlib.sha256(s.encode()).hexdigest(),'assumptions':{'copper_thickness_m':thickness,'resistivity_ohm_m':rho,'note':'segment-only copper estimate; excludes pads, planes, contacts, vias, temperature coefficient, and current distribution; not acceptance closure'},'nets':{}}
for n in target:
 ss=[x for x in segs if x['net']==n]; vs=[x for x in vias if x['net']==n]; zz=[x for x in zones if x['net']==n]
 bylayer={}
 for x in ss:
  q=bylayer.setdefault(x['layer'],{'segments':0,'length_mm':0.0,'min_width_mm':999,'max_width_mm':0,'estimated_ohm':0})
  q['segments']+=1; q['length_mm']+=x['length_mm']; q['min_width_mm']=min(q['min_width_mm'],x['width_mm']); q['max_width_mm']=max(q['max_width_mm'],x['width_mm']); q['estimated_ohm']+=rho*(x['length_mm']/1000)/(x['width_mm']/1000*thickness)
 if not ss: bylayer={}
 out['nets'][n]={'segment_count':len(ss),'total_segment_length_mm':sum(x['length_mm'] for x in ss),'min_segment_width_mm':min((x['width_mm'] for x in ss),default=None),'max_segment_width_mm':max((x['width_mm'] for x in ss),default=None),'via_count':len(vs),'via_drills_mm':sorted(set(round(x['drill_mm'],4) for x in vs)),'zones':zz,'by_layer':bylayer,'segment_only_resistance_ohm':sum(rho*(x['length_mm']/1000)/(x['width_mm']/1000*thickness) for x in ss)}
# all power segments by names
out['all_named_power_segment_count']=sum(1 for x in segs if x['net'] in target)
out['all_named_power_via_count']=sum(1 for x in vias if x['net'] in target)
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
# concise report
lines=[f"Source SHA-256: {out['pcb_sha256']}","Method: regex extraction of native segment/via/zone records; 35um 1oz conservative copper-only estimate; excludes pads, plane spreading, contacts, vias, temperature, and current sharing."]
for n,d in out['nets'].items(): lines.append(f"{n}: segments={d['segment_count']} length_mm={d['total_segment_length_mm']:.3f} width_mm={d['min_segment_width_mm']}..{d['max_segment_width_mm']} vias={d['via_count']} zones={len(d['zones'])} copper_only_ohm={d['segment_only_resistance_ohm']:.6g}")
Path(sys.argv[3]).write_text('\n'.join(lines)+'\n')
