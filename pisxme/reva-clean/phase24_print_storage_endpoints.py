"""Print transformed native endpoint coordinates for support-corridor planning."""
import pcbnew
P='pisxme/reva-clean/PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb';b=pcbnew.LoadBoard(P)
for r in ('U11','L10','Y10','C80','C81','C82','C83'):
 f=b.FindFootprintByReference(r);print(r,pcbnew.ToMM(f.GetPosition().x),pcbnew.ToMM(f.GetPosition().y),f.GetOrientationDegrees())
 for p in f.Pads():
  if p.GetNetname().startswith(('JMS_','LXO','XIN','XOUT')): print(' ',p.GetNumber(),p.GetNetname(),pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
u=b.FindFootprintByReference('U11')
for num in ('10','16'):
 p=u.FindPadByNumber(num);print('U11',num,p.GetNetname(),pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
