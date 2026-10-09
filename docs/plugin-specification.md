# Plugin format and OpenAI requirements

The Mibba plugin uses [Agent Plugins 1.0.0](https://agent-plugins.org/specification)
as its portable package format. OpenAI-specific requirements come from OpenAI's
[packaging guide](https://developers.openai.com/plugins/build/plugins) and
[submission reference](https://developers.openai.com/plugins/deploy/submission).
These sources were checked on 9 October 2026.

## Portable package

The authoritative package lives in `plugins/mibba/`:

```text
plugins/mibba/
├── plugin.json
├── mcp.json
├── skills/
│   ├── mibba/SKILL.md
│   ├── dossier-research/SKILL.md
│   ├── document-audit/SKILL.md
│   └── activity-report/SKILL.md
├── assets/logo512.png
└── README.md
```

`plugin.json` declares the canonical plugin schema URL, identity, release version,
publisher, and project links. `mcp.json` declares the canonical MCP schema URL
for the same specification version. Portable clients discover those files and
`skills/` at their fixed root locations. Do not add `interface`, `skills`, or
`mcpServers` at the root of the portable manifest.

The hosted MCP entry uses `type: "streamable-http"` and
`https://mcp.mibba.co/mcp`. OAuth discovery, sign-in, and credential storage belong
to the client and server. Credentials must never enter the package.

Client-specific manifest data belongs under a reverse-domain key in `extensions`.
Client-specific extension files, if added, belong in the corresponding namespace
directory as defined by the common specification.

## OpenAI extension

OpenAI reads its settings from `plugin.json` under `extensions.com.openai`.
The current package includes:

| Setting | Location | Purpose |
| --- | --- | --- |
| Listing | `interface` | Display name, descriptions, developer name, category, capabilities, URLs, prompts, and icons |
| Review scenarios | `review.test_cases` | Five positive and three negative cases for the single MCP server |
| Commerce | `review.commerce` and `review.commerce_description` | Describe whether the plugin supports commerce |
| Release notes | `publication.release_notes` | Describe the submitted release |
| Translations | `publication.translations.fr-FR` | French subtitle and description |

OpenAI's submission limits include a 30-character display name and short
description, a 4000-character long description, and an 80-character developer
name. Include privacy, support, terms, and website URLs. Starter prompts support
up to three entries of at most 128 characters each. The package uses a 512-pixel
square PNG for both `logo` and `composerIcon`.

`onboardingSkill` is optional. If added, its value must be a `./`-prefixed path
to a packaged `SKILL.md`. It is currently omitted; the `mibba` skill already
provides an introduction when invoked.

Initial MCP review also needs a reviewer-accessible video walkthrough and access
to a dedicated demo account with synthetic data. The packaged scenarios are
definitions that still need to be run. Enter credentials and reviewer sign-in
instructions in the dashboard's secure Review details form. Add the real video
URL there, or later as `review.demo_recording_url`. Do not put placeholder URLs,
credentials, `test_credentials`, or `reviewer_instructions` in the manifest.

## Compatibility and precedence

`.codex-plugin/plugin.json` and `.mcp.json` remain for older Codex clients.
`.claude-plugin/plugin.json` and `mcp.claude.json` remain for Claude Code.
Their native HTTP configuration uses `type: "http"`; the portable MCP file uses
`type: "streamable-http"`.

When root `extensions.com.openai` exists, OpenAI uses that whole object and
ignores the Codex compatibility manifest's settings. It does not merge the two.
If that object is absent, the compatibility manifest supplies OpenAI settings.
Root identity, `skills/`, and `mcp.json` remain authoritative for a portable
package in either case.

Update the root manifest first, then mirror its identity, listing, review, and
publication values into the Codex compatibility manifest. Keep all MCP endpoints
in agreement. The packaging script rejects differences so an older client cannot
silently receive stale metadata.

The existing README already referenced
[Paper Design's agent plugins](https://github.com/paper-design/agent-plugins).
Use Paper's manifests as examples of multi-client packaging. They are not the
normative schema and do not establish OpenAI submission requirements.

## Validate and build

From the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/package-openai.py
```

The script validates the root manifest and MCP configuration against the official
JSON Schemas vendored in `schemas/agent-plugins/1.0.0/`. Those files are unchanged
copies of the [canonical schemas](https://agent-plugins.org/schemas). Validation
uses local schemas and requires no network access after dependencies are installed.
The script also checks compatibility metadata, the expected MCP endpoint, listing
limits, review cases, skills, icon dimensions, and ZIP integrity.

The ZIP contains root `plugin.json`, `mcp.json`, the skills, logo, README, and
license. It excludes compatibility manifests and marketplace files. CI builds
the same ZIP and uploads it as the `mibba-openai` artifact. A successful build
checks packaging; portal validation and authenticated demo tests are separate.
