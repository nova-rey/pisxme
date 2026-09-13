import pcbnew, pathlib, hashlib, json
root=pathlib.Path('/workspace/project')
pcb=root/'pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
board=pcbnew.LoadBoard(str(pcb))
changes={
 'U13':((180.0,135.0),180.0),
 'C30':((103.5,116.0),180.0),
 'C32':((103.5,120.0),180.0),
 'C33':((103.5,128.0),180.0),
 'C31':((103.5,132.0),180.0),
 'F2':((18.0,145.0),None),
 'D2':((35.0,145.0),None),
}
out=[]
for ref,(pos,rot) in changes.items():
 f=board.FindFootprintByReference(ref)
 if f is None: raise SystemExit(f'missing {ref}')
 before=(f.GetPosition().x/1e6,f.GetPosition().y/1e6,float(f.GetOrientationDegrees()))
 f.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(pos[0]),pcbnew.FromMM(pos[1])))
 if rot is not None: f.SetOrientationDegrees(rot)
 after=(f.GetPosition().x/1e6,f.GetPosition().y/1e6,float(f.GetOrientationDegrees()))
 out.append({'ref':ref,'before':before,'after':after})
board.Save(str(pcb))
sha=hashlib.sha256(pcb.read_bytes()).hexdigest()
(pathlib.Path('/workspace/receipts')).mkdir(exist_ok=True)
(pathlib.Path('/workspace/receipts/placement.json')).write_text(json.dumps({'pcb':pcb.name,'sha256':sha,'changes':out},indent=2))
print(json.dumps({'pcb':str(pcb),'sha256':sha,'changes':out},indent=2))
