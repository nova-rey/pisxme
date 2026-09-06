"""Create a disposable J7-to-authoritative-TI-U7 USB3 geometry fixture."""
from pathlib import Path
import argparse, pcbnew

def main():
    ap=argparse.ArgumentParser();ap.add_argument('pcb');ap.add_argument('output');a=ap.parse_args()
    b=pcbnew.LoadBoard(a.pcb)
    tracks=list(b.GetTracks());zones=list(b.Zones())
    for f in list(b.GetFootprints()):
        if f.GetReference() not in {'J7','U7'}: b.Remove(f)
    for t in tracks: b.RemoveNative(t)
    for z in zones: b.RemoveNative(z)
    b.BuildListOfNets();b.Save(a.output);print(a.output)
if __name__=='__main__':main()
