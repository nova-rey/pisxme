"""Focused regression for the official-CM5IO MDI geometry transplant."""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parents[2]
BOARD = Path(os.environ.get("PISXME_ETHERNET_FIXTURE", ROOT / "pisxme/reva-clean/CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb"))
PAIRS = {f"CM5_GBE_TD{i}_{p}" for i in range(4) for p in "PN"}

def mm(v): return pcbnew.ToMM(v)

def main():
    b = pcbnew.LoadBoard(str(BOARD)); lengths = {n: 0.0 for n in PAIRS}; tracks = {n: 0 for n in PAIRS}
    for t in b.GetTracks():
        n=t.GetNetname()
        if n not in PAIRS: continue
        assert t.GetLayer() == pcbnew.F_Cu, (n, t.GetLayerName())
        assert abs(mm(t.GetWidth()) - .127) < .001, (n, mm(t.GetWidth()))
        a=t.GetStart(); z=t.GetEnd(); lengths[n] += ((mm(z.x-a.x)**2 + mm(z.y-a.y)**2) ** .5); tracks[n]+=1
    assert all(tracks.values()), tracks
    for fref, mapping in {
        "J7": {3:"CM5_GBE_TD3_P",4:"CM5_GBE_TD1_P",5:"CM5_GBE_TD3_N",6:"CM5_GBE_TD1_N",9:"CM5_GBE_TD2_N",10:"CM5_GBE_TD0_N",11:"CM5_GBE_TD2_P",12:"CM5_GBE_TD0_P"},
        "U6": {1:"CM5_GBE_TD1_P",2:"CM5_GBE_TD1_N",4:"CM5_GBE_TD0_N",5:"CM5_GBE_TD0_P",6:"CM5_GBE_TD0_P",7:"CM5_GBE_TD0_N",9:"CM5_GBE_TD1_N",10:"CM5_GBE_TD1_P"},
        "U9": {1:"CM5_GBE_TD3_P",2:"CM5_GBE_TD3_N",4:"CM5_GBE_TD2_N",5:"CM5_GBE_TD2_P",6:"CM5_GBE_TD2_P",7:"CM5_GBE_TD2_N",9:"CM5_GBE_TD3_N",10:"CM5_GBE_TD3_P"},
        "J2": {1:"CM5_GBE_TD0_P",2:"CM5_GBE_TD0_N",3:"CM5_GBE_TD1_P",6:"CM5_GBE_TD1_N",7:"CM5_GBE_TD2_P",8:"CM5_GBE_TD2_N",9:"CM5_GBE_TD3_P",10:"CM5_GBE_TD3_N"},
    }.items():
        f=b.FindFootprintByReference(fref); assert f is not None, fref
        for pad,name in mapping.items(): assert f.FindPadByNumber(str(pad)).GetNetname() == name, (fref,pad,f.FindPadByNumber(str(pad)).GetNetname(),name)
    for i in range(4):
        skew=abs(lengths[f"CM5_GBE_TD{i}_P"]-lengths[f"CM5_GBE_TD{i}_N"])
        assert skew < 2.0, (i,skew)
    print("CM5IO transplant MDI regression: PASS")
    print("tracks=" + str(tracks))
    print("length_mm=" + ", ".join(f"TD{i}={lengths[f'CM5_GBE_TD{i}_P']:.3f}/{lengths[f'CM5_GBE_TD{i}_N']:.3f}" for i in range(4)))

if __name__ == "__main__": main()
