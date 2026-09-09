import pcbnew,sys
b=pcbnew.LoadBoard(sys.argv[1])
for ref in ['J1','J7','U12']:
 f=b.FindFootprintByReference(ref); print(ref, f.GetPosition(), f.GetOrientationDegrees())
 if ref=='J1':
  for p in f.Pads(): print(p.GetNumber(),p.GetNetname(),p.GetPosition().x/1e6,p.GetPosition().y/1e6)
print('tracks near USB3')
for t in b.GetTracks():
 if t.GetNetname() in ('CM5_USB3_RX_N','CM5_USB3_RX_P') and (t.GetStart().y<100e6 or t.GetEnd().y<100e6): print(t.GetNetname(),t.GetLayerName(),t.GetStart().x/1e6,t.GetStart().y/1e6,t.GetEnd().x/1e6,t.GetEnd().y/1e6,t.GetWidth()/1e6)
