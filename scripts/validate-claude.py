#!/usr/bin/env python3
"""Check directory metadata that Claude Code does not enforce."""

import json
import struct
from pathlib import Path
from urllib.parse import urlparse


repo = Path(__file__).resolve().parents[1]
root = repo / "plugins" / "mibba"
manifest = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
marketplace = json.loads((repo / ".claude-plugin" / "marketplace.json").read_text())

if manifest["version"] != marketplace["metadata"]["version"]:
    raise SystemExit("Claude plugin and marketplace versions must match")

icon = (root / manifest["icon"]).resolve()
if not icon.is_relative_to(root.resolve()) or not icon.is_file():
    raise SystemExit("Listing icon must exist inside the plugin")
data = icon.read_bytes()
if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != (512, 512):
    raise SystemExit("Expected the directory's 512 x 512 PNG icon")

for key in ["privacyPolicyUrl", "documentationUrl", "supportUrl", "termsOfServiceUrl"]:
    url = urlparse(manifest[key])
    if url.scheme != "https" or not url.netloc:
        raise SystemExit(f"{key} must be an absolute HTTPS URL")

print(f"Claude directory metadata verified for v{manifest['version']}")
