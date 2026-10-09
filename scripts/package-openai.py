#!/usr/bin/env python3
"""Build the OpenAI upload ZIP from explicit, public plugin components."""

import json
import re
import struct
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

try:
    from jsonschema import Draft202012Validator
except ImportError:
    raise SystemExit("Install validation dependencies: python3 -m pip install -r requirements-dev.txt")


def require(condition, message):
    if not condition:
        raise SystemExit(message)


repo = Path(__file__).resolve().parents[1]
root = repo / "plugins" / "mibba"
manifest_path = root / "plugin.json"
manifest = json.loads(manifest_path.read_text())
schema_root = repo / "schemas" / "agent-plugins" / "1.0.0"
for name in ["plugin", "mcp"]:
    schema = json.loads((schema_root / f"{name}.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    document = json.loads((root / f"{name}.json").read_text())
    errors = list(Draft202012Validator(schema).iter_errors(document))
    require(not errors, f"Invalid {name}.json: " + "; ".join(error.message for error in errors))

openai = manifest["extensions"]["com.openai"]
interface = openai["interface"]
# Older Codex clients still use the compatibility manifest. Reject drift.
legacy = json.loads((root / ".codex-plugin" / "plugin.json").read_text())
expected_legacy = {k: v for k, v in manifest.items() if k != "$schema"}
expected_legacy["extensions"] = {
    **manifest["extensions"],
    "com.openai": {k: v for k, v in openai.items() if k != "interface"},
}
expected_legacy.update(interface=interface, skills="./skills/", mcpServers="./.mcp.json")
require(legacy == expected_legacy, "Codex compatibility manifest differs from root plugin.json")
require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"]), "Invalid plugin name")
require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Invalid release version")
for key, limit in [("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80)]:
    require(0 < len(interface[key].strip()) <= limit, f"Invalid {key} length")
for key in ["websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"]:
    require(interface[key].startswith("https://") and len(interface[key]) <= 1024, f"Invalid {key}")
require(len(interface["defaultPrompt"]) <= 3, "At most three starter prompts are supported")
require(all(0 < len(p) <= 128 for p in interface["defaultPrompt"]), "Invalid starter prompt length")

cases = openai["review"]["test_cases"]
require(len(cases["positive"]) == 5 and len(cases["negative"]) == 3, "Expected five positive and three negative review cases")
for case in cases["positive"]:
    require(all(case.get(k) for k in ["description", "prompt", "tools_triggered", "expected_behavior"]), "Incomplete positive review case")
for case in cases["negative"]:
    require(case.get("description") and case.get("prompt"), "Incomplete negative review case")
mcp = json.loads((root / "mcp.json").read_text())
require(mcp == {
    "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
    "mcpServers": {"mibba": {"type": "streamable-http", "url": "https://mcp.mibba.co/mcp"}},
}, "Unexpected MCP configuration; credentials must stay outside the ZIP")
legacy_mcp = {"mcpServers": {"mibba": {"type": "http", "url": mcp["mcpServers"]["mibba"]["url"]}}}
for name in [".mcp.json", "mcp.claude.json"]:
    require(json.loads((root / name).read_text()) == legacy_mcp, f"{name} differs from portable MCP configuration")

assets = set()
for key in ["logo", "composerIcon"]:
    require(interface[key] == "./assets/logo512.png", f"Unexpected {key} path")
    asset = root / interface[key]
    data = asset.read_bytes()
    require(data[:8] == b"\x89PNG\r\n\x1a\n", "Expected a PNG icon")
    width, height = struct.unpack(">II", data[16:24])
    require(width == height and 48 <= width <= 4096 and len(data) <= 5 * 1024 * 1024, "Invalid icon dimensions or size")
    assets.add(asset)

skills = sorted((root / "skills").glob("*/SKILL.md"))
require({skill.parent.name for skill in skills} == {"mibba", "dossier-research", "document-audit", "activity-report"}, "Expected the introduction and three Mibba research skills")
for skill in skills:
    text = skill.read_text()
    require(text.startswith("---\n") and "\nname: " in text and "\ndescription: " in text, f"Missing frontmatter: {skill}")

# Use an allowlist rather than archiving the checkout or alternate client files.
files = sorted({manifest_path, root / "mcp.json", root / "README.md", *assets, *skills})
require(all(f.is_file() and not f.is_symlink() and f.resolve().is_relative_to(root.resolve()) for f in files), "Package members must be regular files inside the plugin")
output = repo / "dist" / f"mibba-openai-{manifest['version']}.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for file in files:
        archive.write(file, file.relative_to(root).as_posix())
    archive.write(repo / "LICENSE", "LICENSE")
with ZipFile(output) as archive:
    require(archive.testzip() is None, "ZIP integrity check failed")
    print(f"Created {output} ({output.stat().st_size:,} bytes; {len(archive.namelist())} files)")
print("Review scenarios are packaged but must still be run against the demo account before submission.")
