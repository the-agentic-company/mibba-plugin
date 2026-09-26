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
    ├── .mcp.json
    ├── mcp.claude.json
    └── skills/
```

See [plugins/mibba/README.md](plugins/mibba/README.md) for capabilities and data-access details.

## Maintainer references

When changing plugin packaging or marketplace metadata, use
[paper-design/agent-plugins](https://github.com/paper-design/agent-plugins) as a maintained
multi-client layout example, especially its
[Claude manifest](https://github.com/paper-design/agent-plugins/blob/main/plugins/paper-desktop/.claude-plugin/plugin.json).
For normative behavior, also check the
[Claude plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)
and the [Agent Plugins specification](https://agent-plugins.org/specification).

The Claude directory portal also requests listing metadata that is not part of the Claude plugin
manifest. Keep these values in the portal rather than adding unknown fields to `plugin.json`:

- Icon: `plugins/mibba/assets/logo512.png`
- Short description: `Travaillez avec vos dossiers notariaux Mibba directement dans Claude.`
- Documentation: `https://mibba.co/docs/installer-le-plugin-mibba`
- Support: `https://mibba.co/contact`
- Privacy policy: `https://mibba.co/politique-de-confidentialite`
- Terms of service: `https://mibba.co/conditions-generales-utilisation`

Run `claude plugin validate --strict plugins/mibba` after manifest changes. Unknown top-level
fields are stripped by Claude Code and fail strict validation.
