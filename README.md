### Tom Vaucourt

AI engineer — Local inference and agentic developer tooling. I build end-to-end systems and contribute upstream to the tools I depend on.

**Now:** [Starbridge](https://github.com/T0mSIlver/starbridge), so a coding agent that stops for a question reaches you on your phone, live at [starbridge.run](https://starbridge.run). Still shipping voice for coding agents in [localvoxtral](https://github.com/T0mSIlver/localvoxtral).

#### Selected work

- **[Starbridge](https://github.com/T0mSIlver/starbridge)** — when a coding agent (Claude Code, Codex, Pi, opencode) stops for a question, Starbridge puts it on your phone and in your browser. You answer with one tap and the session carries on. It also shows what's left on each AI plan, read from CodexBar. The server stores your content only as ciphertext, though it still sees [who sent what, and when](https://starbridge.run/docs/faq#what-does-the-server-see). Free server at [starbridge.run](https://starbridge.run), or host your own. `TypeScript` `Kotlin`
- **[vidtheque](https://github.com/T0mSIlver/vidtheque)** — the talks you don't have time to watch, queryable by an agent over MCP: transcripts, on-screen text and keyframes, every answer stamped with the second it happened. Self-hosted, with a [demo](https://vidtheque.dev/demo) that indexes 310 AI Engineer talks and [both days of AI Engineer Paris 2026](https://vidtheque.dev/paris). `Python` `JavaScript`
- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)** — native macOS menu-bar app for realtime, fully local dictation. Words appear while you're still speaking. Built for prompting coding agents by voice, it grounds LLM polishing in the session under your cursor, its screen and the repo's vocabulary. `Swift`
- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)** — eight merged PRs on the Voxtral realtime streaming path: incremental mel/conv front end (O(N²) → O(N)), in-place KV append and token-by-token decode for bounded memory, and the [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) I publish. Streaming went from ~1.9× slower than realtime to 0.76 RTF. `Swift`
- **[working-set](https://github.com/T0mSIlver/working-set)** — how many agents a given GPU configuration keeps warm, and which constraint binds first: KV cache, decode bandwidth, or prefill compute. A scenario model on PyPI (`ws predict`, `ws test` on a live vLLM endpoint) behind an [explorer](https://workingset.tomvaucourt.com/) that answers with a verdict. `Python` `HTML`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)** — merged: preserve Anthropic thinking blocks through the server's message conversion. `C++`
- **[skills](https://github.com/T0mSIlver/skills)** — the agent skills I run across Claude Code, Codex, opencode and pi: delegating work to another CLI, Remote Control servers under systemd, prose cleanup. Each one is a gotcha backed by evidence, deleted once upstream fixes it. `Shell`

#### Recently in other projects

<!-- recent_contributions starts -->
- ![Merged pull request](icons/pr_merged.svg) [Cursor: read cursor-agent's login on Linux](https://github.com/steipete/CodexBar/pull/4397) `steipete/CodexBar`
- ![Closed issue](icons/issue_closed.svg) [Claude CLI source: "Missing Current session." when the /usage panel is taller than the 50-row PTY](https://github.com/steipete/CodexBar/issues/4391) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(claude): keep a tall /usage panel on the PTY screen](https://github.com/steipete/CodexBar/pull/4392) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [README: add Starbridge to integrations](https://github.com/steipete/CodexBar/pull/4371) `steipete/CodexBar`
- ![Open issue](icons/issue_open.svg) [Plugin userConfig options are not expanded in http hook headers (${CLAUDE_PLUGIN_OPTION_*} resolves empty)](https://github.com/anthropics/claude-code/issues/81742) `anthropics/claude-code`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): offer Monthly Plan in the menu bar metric picker](https://github.com/steipete/CodexBar/pull/4072) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): price billing usage by event type, zone, and tier](https://github.com/steipete/CodexBar/pull/4076) `steipete/CodexBar`
- ![Open pull request](icons/pr_open.svg) [Nemotron streaming: compute only new mel frames; keep MLX's buffer cache between steps](https://github.com/Blaizzy/mlx-audio-swift/pull/274) `Blaizzy/mlx-audio-swift`
<!-- recent_contributions ends -->

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver) · [PyPI](https://pypi.org/user/T0mSIlver/)
