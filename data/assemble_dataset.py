#!/usr/bin/env python3
"""Rebuild AIID_Excel_Export-20261005.xlsx from base64 parts (if used)."""
from pathlib import Path
import base64
here = Path(__file__).resolve().parent
parts = sorted(here.glob('AIID_Excel_Export-20261005.part_*.b64'))
if not parts:
    raise SystemExit('No part_*.b64 files found')
data = ''.join(p.read_text() for p in parts)
out = here / 'AIID_Excel_Export-20261005.xlsx'
out.write_bytes(base64.b64decode(data))
print(f'Wrote {out} ({out.stat().st_size} bytes)')
