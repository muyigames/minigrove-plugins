# MiniGrove plugins

Manage your MiniGrove projects from Codex's native conversation. Existing project computers execute the work.

## Install in Codex

Add this public repository as a plugin marketplace:

```sh
codex plugin marketplace add muyigames/minigrove-plugins
codex plugin add minigrove@minigrove-plugins
```

Open the Plugins Directory, choose the MiniGrove source and install MiniGrove. Complete browser sign-in, select projects and authorize the actions you want. Start a new chat after installation. Creating tasks has its own permission; existing grants need authorization again before that tool appears.

For a direct MCP connection, use [MiniGrove's setup guide](https://app.minigrove.io/mcp/connect) or:

```sh
codex mcp add minigrove --url https://app.minigrove.io/mcp
codex mcp login minigrove
```

Try: “List my authorized MiniGrove projects and summarize active tasks.” For a new task, name the project and existing computer. The first instruction starts automatically; do not send it twice. Follow workspace preparation through the actual execution and result.

[Workflow and recovery](plugins/minigrove/README.md) · [Privacy](https://app.minigrove.io/privacy) · [Terms](https://app.minigrove.io/terms) · [Help](https://app.minigrove.io/get-started)

## Build the ZIP

```sh
python3 scripts/package-plugin.py
```

The standard-library-only packager prints the output path and SHA256. The ZIP contains the plugin manifest, MCP configuration, workflow skill, guide and brand marks.

This repository is a public installation source. Universal directory review and listing are a separate process. Availability of repository sources varies by client; the authenticated MCP service is also usable directly.

Version 0.2.1 adds public listing metadata and the existing MiniGrove brand marks to the 0.2.0 workflow. It contains no server implementation or credentials.
