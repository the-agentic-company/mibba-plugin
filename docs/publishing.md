# Directory publishing

## OpenAI

Build the portable ZIP as described in
[Plugin format and OpenAI requirements](plugin-specification.md#validate-and-build).
The `Plugin checks` workflow validates and uploads `mibba-openai` alongside the
Claude archive. Upload the ZIP through [OpenAI Plugins](https://platform.openai.com/plugins),
resolve portal findings, verify the MCP domain, and test OAuth with the demo account.
Complete reviewer access and the video walkthrough before submitting for review.
Packaging success does not confirm runtime authentication or directory approval.

## Claude

The directory tracks `main` in `the-agentic-company/mibba-plugin`, with the plugin at
`plugins/mibba`. Bump the Claude plugin and marketplace versions together when
releasing changes. The `Plugin checks` workflow validates both manifests and the
directory metadata and uploads the Claude plugin archive for review.

Run the same checks locally before pushing:

```sh
python3 scripts/validate-claude.py
```

Install Claude Code first if it is missing. The script runs `claude plugin validate
--strict` on the plugin and marketplace, then checks the directory metadata. Strict
mode fails on warnings as well as errors. CI runs this script on pull requests and
pushes to `main`, and packages the plugin only after validation succeeds.

GitHub webhook `694025284` sends signed `push` deliveries to Anthropic. The directory
fetches the tracked branch, validates it, scans it, and publishes eligible versions
according to the portal's auto-publish setting. A green GitHub workflow does not
confirm that Anthropic has published the version. Check the directory's version
history for that status.

The webhook URL and signing secret are stored in EU Infisical, project
`17910b99-1708-43e4-83bf-d8c4e2766171`, environment `prod`, at the root `/` and in
the `/mibba-plugin` folder:

- `CLAUDE_DIRECTORY_WEBHOOK_URL`
- `CLAUDE_DIRECTORY_WEBHOOK_SECRET`

GitHub signs native deliveries with the secret configured on the webhook. CI needs
no copy of it and no access to the application's secrets. The Mibba repository's
OIDC identity is bound to that repository and must not be reused here. The Infisical
organization currently cannot create another identity because its plan limit has
been reached.

To inspect deliveries without exposing credentials:

```sh
gh api repos/the-agentic-company/mibba-plugin/hooks/694025284/deliveries \
  --jq '.[] | {id, event, status_code, status, delivered_at}'
```

If a delivery fails, fix the cause and redeliver its ID from GitHub's webhook
settings or `POST /repos/the-agentic-company/mibba-plugin/hooks/694025284/deliveries/DELIVERY_ID/attempts`.

The directory submission page requires a paid Claude account with access to the
submission. It is available at
[Mibba submission](https://claude.ai/directory/manage/plugins/ad83ff60-6077-477c-a220-6226c112860a?tab=versions).
