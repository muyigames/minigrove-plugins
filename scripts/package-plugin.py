#!/usr/bin/env python3
"""Build the MiniGrove plugin ZIP with the Python standard library."""
import hashlib
import json
from pathlib import Path
import zipfile

repo = Path(__file__).resolve().parent.parent
root = repo / 'plugins/minigrove'
manifest = json.loads((root / '.codex-plugin/plugin.json').read_text())
files = ['.codex-plugin/plugin.json', '.mcp.json', 'README.md',
         'skills/manage-minigrove/SKILL.md', 'assets/icon.svg', 'assets/icon-dark.svg']
out = repo / 'dist' / f"minigrove-{manifest['version']}.zip"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for name in sorted(files):
        path = root / name
        assert not path.is_symlink() and path.resolve().is_relative_to(root)
        entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        archive.writestr(entry, path.read_bytes())
with zipfile.ZipFile(out) as archive:
    assert archive.testzip() is None and len(archive.namelist()) == len(files)
print(out)
print('SHA256 ' + hashlib.sha256(out.read_bytes()).hexdigest())
