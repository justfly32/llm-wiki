---
source_url: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
ingested: 2026-07-15
type: hn_article
hn_id: 48905248
hn_score: 312
hn_author: shintoist
---

# How to stop Claude from saying load-bearing

**Score:** 312 | **By:** shintoist | **Comments:** 400
**URL:** https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
**HN:** https://news.ycombinator.com/item?id=48905248

## Content

How to stop Claude from saying load-bearing | jola.dev jola.dev Home About Blog Newsletter Projects Talks Home About Blog Newsletter Projects Talks How to stop Claude from saying load-bearing July 14, 2026 2 min read claude llm parody Absolutely ripping your hair out reading Claude referring to everything as “honest takes” and &quot;load-bearing seams&quot;? You’re not the only one . But what if I tell you there’s a way to take this massive source of frustration and make it so ridiculous you can't but laugh at it? Or just simply fix Claude's vocabulary. I present to you, the MessageDisplay hook. First you need a little script with some replacements set up: #!/usr/bin/env python3 import json , re , sys replacements = { &quot;seam&quot;: &quot;whatchamacallit&quot; , &quot;you&#39;re absolutely right&quot;: &quot;I&#39;m a complete clown&quot; , &quot;honest take&quot;: &quot;spicy doodad&quot; , &quot;load-bearing&quot;: &quot;cooked&quot; } data = json . load ( sys . stdin ) text = data . get ( &quot;delta&quot; ) or &quot;&quot; for phrase , replacement in replacements . items ( ) : pattern = r &quot; \b &quot; + re . escape ( phrase ) + r &quot; \b &quot; text = re . sub ( pattern , replacement , text , flags = re . IGNORECASE ) print ( json . dumps ( { &quot;hookSpecificOutput&quot;: { &quot;hookEventName&quot;: &quot;MessageDisplay&quot; , &quot;displayContent&quot;: text , } } ) ) put that in ~/.claude/hooks/wordswap.sh and make it executable with chmod +x ~/.claude/hooks/wordswap.sh . Then to hook it up, add it to your ~/.claude/settings.json in the hooks block like: { &quot;hooks&quot; : { &quot;MessageDisplay&quot; : [ { &quot;hooks&quot; : [ { &quot;type&quot; : &quot;command&quot; , &quot;command&quot; : &quot;$HOME/.claude/hooks/wordswap.sh&quot; } ] } ] } } Hooks load at startup, so you just need to start a new session to start your new life. I'm sure you can come up with much better and more productive replacements than me. Have fun! Written by Johanna Larsson . Thoughts on this post? Find me on Bluesky at @jola.dev . Like this post? Support my writing on GitHub Sponsors and get a monthly newsletter with content from the blog, or buy me a coffee on Ko-fi. 🙏 Sponsor me on GitHub ☕ Buy me a coffee on Ko-fi Related posts Let libraries be libraries July 07, 2026 A gentle rant on the topic of libraries that run as Elixir applications and why that&#39;s an anti-pattern for library design. elixir oss CI workflows on Tangled for Elixir July 04, 2026 How to set up CI workflows on Tangled for Elixir, with specific Elixir and Erlang versions, and a PostgreSQL service. atproto tangled Automatically syncing your blog to atproto and standard.site June 29, 2026 Kicking off a little side project for automatically discovering content through blog post feeds and syncing to atproto and standard.site. blog atproto Back to all posts Architecting © 2026 Johanna Larsson. All rights reserved.
