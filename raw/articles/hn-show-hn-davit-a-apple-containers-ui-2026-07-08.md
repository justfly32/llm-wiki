---
source_url: https://davit.app
ingested: 2026-07-08
type: hn_article
hn_id: 48821848
hn_score: 34
hn_author: xinit
---

# Show HN: Davit, a Apple Containers UI

**Score:** 34 | **By:** xinit | **Comments:** 6
**URL:** https://davit.app
**HN:** https://news.ycombinator.com/item?id=48821848

## Content

Davit — a native macOS UI for Apple containers Davit A fully native macOS app for Apple's container platform — run Linux containers on Apple silicon, no Docker Desktop required. Free &amp; open source · MIT licensed · Signed &amp; notarized Download for macOS View on GitHub Requires an Apple silicon Mac running macOS 15 or later. Or via Homebrew: brew install wouterdebie/tap/davit The dashboard: services, disk usage and live CPU across all running containers. Everything you'd expect. Nothing you don't. Davit talks directly to Apple's open-source container daemon over XPC — the same wire path the CLI uses. No Electron, no web views, no background agents of its own. 📦 Containers Start, stop, restart and delete with live CPU, memory and IP on every row. Streaming logs with follow &amp; boot mode, live stat charts, and raw config inspection. 🖥️ One-click terminal Open an interactive shell in any running container, straight into Terminal or iTerm — over the native API, no CLI needed. 🪄 Edit &amp; Recreate Containers are immutable — so Davit prefills a new one from the old config with the image's entrypoint and env subtracted, letting you change ports, env vars, mounts or resources in seconds. 💿 Images, volumes, networks Pull with live progress, run from any image, tag, prune. Create sized volumes and custom subnets. See what's in use before you delete it. ⚙️ Platform settings, editable Default CPU/memory for new containers, registry, DNS, builder resources — edited in the app, validated by the platform's own config loader, saved as clean TOML overrides. ⬇️ Installs the platform for you No container platform installed? Davit downloads Apple's signed installer, verifies it, and sets everything up in your user Library — no administrator rights needed . It can add the container CLI to your shell, too. Native, down to the pixels. Built entirely in SwiftUI. Menu bar quick actions, a Dock icon only when you want one, and live charts that don't spin up a browser to render. Containers with live stats and port badges. Per-container CPU &amp; memory, sampled every 2 seconds. Network, ports, mounts and environment at a glance. Images with sizes, platforms and in-use badges. How is this different from Docker Desktop? It's Apple's engine. Each container runs in its own lightweight VM via Apple's Virtualization framework — sub-second boots, per-container IP addresses, optimized for Apple silicon. OCI all the way. Pulls from Docker Hub, ghcr.io, quay.io or any registry. Your existing images just work. Nothing between you and the daemon. Davit links Apple's own client library and speaks XPC directly — no socket shims, no license agreements, no accounts. Tiny. A single ~17 MB app. Davit is free software, MIT licensed . Built on apple/container . GitHub · Download · Issues © 2026 Wouter de Bie
