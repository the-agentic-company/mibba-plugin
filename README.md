# Mibba agent plugins

Use Mibba with Codex and Claude Code. The shared plugin connects to Mibba's hosted OAuth MCP server and adds focused skills for notarial dossier research.

## Codex

Add the marketplace:

```sh
codex plugin marketplace add the-agentic-company/mibba-plugin
```

Install the plugin:

```sh
codex plugin add mibba@mibba
```

## Claude Code

Add the marketplace:

```text
/plugin marketplace add the-agentic-company/mibba-plugin
```

Install the plugin:

```text
/plugin install mibba@mibba
```

Then run `/reload-plugins` if Claude asks you to reload.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
└── plugins/mibba
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    ├── plugin.json
    ├── mcp.json
    ├── .mcp.json
    ├── mcp.claude.json
    └── skills/
```

See [plugins/mibba/README.md](plugins/mibba/README.md) for capabilities and data-access details.

## OpenAI public directory submission

Build the ChatGPT and Codex submission ZIP from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/package-openai.py
```

The ZIP in `dist/` uses Agent Plugins 1.0.0 and includes the root manifest,
portable hosted MCP configuration, four skills,
listing icon, README, and license. It excludes marketplace files, alternate client
manifests, repository history, and local credentials. The script checks listing limits,
review-case counts, compatibility metadata, icon dimensions, and archive integrity.
It also validates the portable files against the vendored official JSON Schemas.

Upload it through [OpenAI Plugins](https://platform.openai.com/plugins) under the
appropriate verified developer identity. Follow the
[submission guide](https://developers.openai.com/plugins/deploy/submission) to resolve
automated findings, verify the MCP domain, and connect the OAuth server.

The five positive and three negative review scenarios in the manifest are prepared
test definitions, not recorded test results. Run them using a dedicated demo account
with synthetic sample data, including an act with cited annexes and supported source
dates. Enter reviewer credentials and sign-in instructions only in the portal's
secure Review details form. Add an accessible video walkthrough URL there before
submitting for review; it is intentionally absent from the public package until a
real recording is available.

## Maintainer references

Use the [Agent Plugins specification](https://agent-plugins.org/specification)
for the portable format and official client documentation for client requirements.
[Plugin format and OpenAI requirements](docs/plugin-specification.md) records the
file layout, OpenAI metadata, compatibility precedence, validation, and submission
requirements. [paper-design/agent-plugins](https://github.com/paper-design/agent-plugins)
is an example of multi-client packaging.

For Claude-specific behavior, use the
[Claude plugin manifest reference](https://code.claude.com/docs/en/plugins-reference).

The Claude directory reads additional listing metadata. Keep the following fields
in `plugins/mibba/.claude-plugin/plugin.json` to satisfy directory policy:

- Icon: `plugins/mibba/assets/logo512.png`
- Privacy policy: `https://mibba.co/politique-de-confidentialite`

Keep the remaining directory-only values in the portal:

- Short description: `iNot, Fiducial dans Claude`
- Documentation: `https://mibba.co/docs/installer-le-plugin-mibba`
- Support: `https://mibba.co/contact`
- Terms of service: `https://mibba.co/conditions-generales-utilisation`

Run `claude plugin validate --strict plugins/mibba` after manifest changes.
