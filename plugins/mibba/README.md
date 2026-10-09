# Mibba plugin

Connect ChatGPT, Codex, or Claude Code to the notarial dossiers and documents that your Mibba account is authorized to access.

## Prerequisites

- A Mibba account with access to at least one workspace.
- A supported ChatGPT, Codex, or Claude Code client with plugin and remote MCP support.

## Features

- Find dossiers, participants, properties, and document inventories.
- Search document text and page-level evidence with Mibba-provided citations.
- Audit cited pieces and calculate supported dossier deadlines.
- Produce complete monthly and annual dossier-activity reports.

When the agent first uses a Mibba tool, complete the Mibba sign-in and authorization flow in the browser.

## Skills

- `mibba`: introduction to Mibba and guidance for retrieving synchronized iNot or Fiducial information through the Mibba MCP. Claude Code exposes it as `/mibba:mibba`; command naming depends on the client.
- `dossier-research`: evidence-backed dossier and document research.
- `document-audit`: inventory, cited-piece, and deadline audits.
- `activity-report`: complete bounded-period activity reports.

## Data access and privacy

This plugin contains no executable code, hooks, telemetry, or local credential handling. It connects only to `https://mcp.mibba.co/mcp`.

The agent sends the arguments of approved Mibba tool calls to Mibba. Mibba returns data from the workspace authorized during OAuth sign-in. The server checks the signed-in user's current workspace membership and scopes every query to that workspace. ChatGPT, Codex, or Claude handles returned data according to the terms of the product you use.

You can revoke the connection from Mibba or your agent's connector settings. Disabling or uninstalling the plugin stops the agent from loading its skills and MCP configuration.

## Support

Visit [Mibba support](https://mibba.co/contact). Read the [privacy policy](https://mibba.co/politique-de-confidentialite) and [terms of use](https://mibba.co/conditions-generales-utilisation).
