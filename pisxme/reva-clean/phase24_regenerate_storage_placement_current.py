"""Regenerate a disposable storage placement using the live authority maps."""
import phase24_place_dual_mode_storage_island as generator
from pathlib import Path

generator.OUT = Path(__file__).resolve().parent / 'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb'
generator.main()
