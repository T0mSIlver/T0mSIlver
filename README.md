### Tom Vaucourt

AI engineer. I work on realtime speech on Apple Silicon and local GPUs, and on the tools I use to run coding agents. I fix the upstream code I depend on and measure the result.

**Now:** the Voxtral Realtime streaming path in [mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift), and [localvoxtral](https://github.com/T0mSIlver/localvoxtral), dictation for prompting coding agents by voice.

#### Voice

- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)**. Eight merged PRs on the Voxtral Realtime streaming path. An incremental mel and conv front end took per-utterance work from O(N²) to O(N), and in-place KV append with token-by-token decode keeps memory flat. Streaming went from about 1.9× slower than realtime to 0.76 RTF, and live text now keeps up for three hours instead of falling behind after fifteen minutes. I also publish the [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) it loads. `Swift` `MLX`
- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)**. A native macOS menu-bar app for realtime dictation, local or against any OpenAI Realtime-compatible server. Words appear while you're still speaking. It finds the Claude Code session under your cursor and polishes the text against that session's screen and the repo's vocabulary. People I don't know use it and file issues. `Swift`
- **[Self-hosted Voxtral STT for LiveKit Agents](https://github.com/T0mSIlver/agents/tree/feat/mistralai-self-hosted-stt)**. `mistralai.SelfHostedSTT` streams a LiveKit voice agent's audio to Voxtral Realtime on your own vLLM server, with no API key. On an RTX 3090 the final transcript lands 466 to 540 ms after the end of speech, over five runs. `Python`

#### Agent tooling

- **[Starbridge](https://github.com/T0mSIlver/starbridge)**. When a coding agent (Claude Code, Codex, Pi, opencode) stops for a question, Starbridge puts it on your phone and in your browser. You answer with one tap and the session carries on. The server stores your content only as ciphertext, though it still sees [who sent what, and when](https://starbridge.run/docs/faq#what-does-the-server-see). Free server at [starbridge.run](https://starbridge.run), or host your own. `TypeScript` `Kotlin`
- **[working-set](https://github.com/T0mSIlver/working-set)**. How many agents a given GPU configuration keeps warm, and which constraint binds first: KV cache, decode bandwidth or prefill compute. A scenario model on PyPI (`ws predict`, `ws test` against a live vLLM endpoint) behind an [explorer](https://workingset.tomvaucourt.com/) that answers with a verdict. `Python`
- **[vidtheque](https://github.com/T0mSIlver/vidtheque)**. Conference talks an agent can query over MCP: transcripts, on-screen text and keyframes, each answer stamped with the second it was said. Self-hosted, with a [demo](https://vidtheque.dev/demo) over 310 AI Engineer talks and [both days of AI Engineer Paris 2026](https://vidtheque.dev/paris). `Python`
- **[skills](https://github.com/T0mSIlver/skills)**. The agent skills I run across Claude Code, Codex, opencode and pi. Each one fixes a mistake I saw an agent make, and goes once upstream fixes it. `Shell`

#### Upstream

- **[CodexBar](https://github.com/steipete/CodexBar/pulls?q=is%3Apr+author%3AT0mSIlver+is%3Amerged)**. Eight merged PRs: Mistral plan usage and billing, a tall Claude `/usage` panel, cursor-agent's login on Linux. `Swift`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)**. Merged: the server keeps Anthropic thinking blocks through its message conversion. `C++`

#### Recently in other projects

<!-- recent_contributions starts -->
- ![Closed issue](icons/issue_closed.svg) [TUI segfaults on small-ICU Node builds (Intl.Segmenter null deref) — RHEL nodejs without nodejs-full-i18n](https://github.com/earendil-works/pi/issues/6359) `earendil-works/pi`
- ![Closed issue](icons/issue_closed.svg) [rpiv-ask-user-question: execute never returns when loaded from an esbuild ESM bundle](https://github.com/juicesharp/rpiv-mono/issues/208) `juicesharp/rpiv-mono`
- ![Merged pull request](icons/pr_merged.svg) [fix(rpiv-ask-user-question): no runtime import cycle, so esbuild ESM bundles stop hanging (#208)](https://github.com/juicesharp/rpiv-mono/pull/209) `juicesharp/rpiv-mono`
- ![Merged pull request](icons/pr_merged.svg) [Cursor: read cursor-agent's login on Linux](https://github.com/steipete/CodexBar/pull/4397) `steipete/CodexBar`
- ![Closed issue](icons/issue_closed.svg) [Claude CLI source: "Missing Current session." when the /usage panel is taller than the 50-row PTY](https://github.com/steipete/CodexBar/issues/4391) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(claude): keep a tall /usage panel on the PTY screen](https://github.com/steipete/CodexBar/pull/4392) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [README: add Starbridge to integrations](https://github.com/steipete/CodexBar/pull/4371) `steipete/CodexBar`
- ![Open issue](icons/issue_open.svg) [Plugin userConfig options are not expanded in http hook headers (${CLAUDE_PLUGIN_OPTION_*} resolves empty)](https://github.com/anthropics/claude-code/issues/81742) `anthropics/claude-code`
<!-- recent_contributions ends -->

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver) · [PyPI](https://pypi.org/user/T0mSIlver/)
