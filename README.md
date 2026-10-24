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
- ![Closed issue](icons/issue_closed.svg) [Misc. bug: server: realtime commit completes the item before the flushed words are decoded](https://github.com/ggml-org/llama.cpp/issues/30968) `ggml-org/llama.cpp`
- ![Merged pull request](icons/pr_merged.svg) [Whisper: add a translate task to STTGenerateParameters](https://github.com/Blaizzy/mlx-audio-swift/pull/295) `Blaizzy/mlx-audio-swift`
- ![Merged pull request](icons/pr_merged.svg) [Qwen3-ASR: cap maxTokens per chunk, not per file](https://github.com/Blaizzy/mlx-audio-swift/pull/294) `Blaizzy/mlx-audio-swift`
- ![Open pull request](icons/pr_open.svg) [Core: reuse a cached snapshot that has no config.json](https://github.com/Blaizzy/mlx-audio-swift/pull/296) `Blaizzy/mlx-audio-swift`
- ![Merged pull request](icons/pr_merged.svg) [STT: forward the loadModel cache to the six loaders that dropped it](https://github.com/Blaizzy/mlx-audio-swift/pull/293) `Blaizzy/mlx-audio-swift`
- ![Merged pull request](icons/pr_merged.svg) [Build against mlx-swift main (#469): Parakeet and Qwen3-TTS compile calls](https://github.com/Blaizzy/mlx-audio-swift/pull/292) `Blaizzy/mlx-audio-swift`
- ![Merged pull request](icons/pr_merged.svg) [Nemotron streaming: reuse decoder and encoder work that has not changed](https://github.com/Blaizzy/mlx-audio-swift/pull/275) `Blaizzy/mlx-audio-swift`
- ![Open pull request](icons/pr_open.svg) [feat(mistralai): add SelfHostedSTT for Voxtral Realtime on vLLM](https://github.com/livekit/agents/pull/8016) `livekit/agents`
<!-- recent_contributions ends -->

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver) · [PyPI](https://pypi.org/user/T0mSIlver/)
