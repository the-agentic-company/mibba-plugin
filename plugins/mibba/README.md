# Mibba plugin

Connect Codex or Claude Code to the notarial dossiers and documents that your Mibba account is authorized to access.

## Prerequisites

- A Mibba account with access to at least one workspace.
- A current Codex or Claude Code release with plugin and remote MCP support.

## Features

- Find dossiers, participants, properties, and document inventories.
- Search document text and page-level evidence with Mibba-provided citations.
- Audit cited pieces and calculate supported dossier deadlines.
- Produce complete monthly and annual dossier-activity reports.

When the agent first uses a Mibba tool, complete the Mibba sign-in and authorization flow in the browser.

## Skills

- `dossier-research`: evidence-backed dossier and document research.
- `document-audit`: inventory, cited-piece, and deadline audits.
- `activity-report`: complete bounded-period activity reports.

## Data access and privacy

This plugin contains no executable code, hooks, telemetry, or local credential handling. It connects only to `https://mcp.mibba.co/mcp`.

The agent sends the arguments of approved Mibba tool calls to Mibba. Mibba returns data from the workspace authorized during OAuth sign-in. The server checks the signed-in user's current workspace membership and scopes every query to that workspace. Codex or Claude handles returned data according to the terms of the product you use.

You can revoke the connection from Mibba or your agent's connector settings. Disabling or uninstalling the plugin stops the agent from loading its skills and MCP configuration.

## Support

Visit [mibba.co](https://mibba.co).
