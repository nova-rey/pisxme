"""Disposable co-location of RTL9210B SPI flash U2 with the moved island."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_RAILS_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_U2_V1.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE));f=next(x for x in b.GetFootprints() if str(x.GetReference())=='U2')
 q=f.GetPosition();f.SetPosition(pcbnew.VECTOR2I(q.x-int(15e6),q.y+int(18e6)))
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
