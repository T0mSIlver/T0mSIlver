### Tom Vaucourt

AI engineer — Local inference and agentic developer tooling. I build end-to-end systems and contribute upstream to the tools I depend on.

**Now:** [vidtheque](https://github.com/T0mSIlver/vidtheque), a self-hosted video knowledge base your coding agent can query mid-task, live at [vidtheque.dev](https://vidtheque.dev). Still shipping voice for coding agents in [localvoxtral](https://github.com/T0mSIlver/localvoxtral).

#### Selected work

- **[vidtheque](https://github.com/T0mSIlver/vidtheque)** — the talks you don't have time to watch, queryable by an agent over MCP: transcripts, on-screen text and keyframes, every answer stamped with the second it happened. Self-hosted, with a [demo](https://vidtheque.dev/demo) that indexes 310 AI Engineer talks and [both days of AI Engineer Paris 2026](https://vidtheque.dev/paris). `Python` `JavaScript`
- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)** — native macOS menu-bar app for realtime, fully local dictation. Words appear while you're still speaking. Built for prompting coding agents by voice, it grounds LLM polishing in the session under your cursor, its screen and the repo's vocabulary. `Swift`
- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)** — eight merged PRs on the Voxtral realtime streaming path: incremental mel/conv front end (O(N²) → O(N)), in-place KV append and token-by-token decode for bounded memory, and the [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) I publish. Streaming went from ~1.9× slower than realtime to 0.76 RTF. `Swift`
- **[working-set](https://github.com/T0mSIlver/working-set)** — how many agents a given GPU configuration keeps warm, and which constraint binds first: KV cache, decode bandwidth, or prefill compute. A scenario model on PyPI (`ws predict`, `ws test` on a live vLLM endpoint) behind an [explorer](https://workingset.tomvaucourt.com/) that answers with a verdict. `Python` `HTML`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)** — merged: preserve Anthropic thinking blocks through the server's message conversion. `C++`
- **[fastcontext](https://github.com/T0mSIlver/fastcontext)** — read-only repository-exploration agent that coding agents delegate to over bash: cited `file:line` answers, not context noise. `Python`
- **[toklen](https://github.com/T0mSIlver/toklen)** — count tokens with a model's real Hugging Face tokenizer. `npx toklen` and `uvx toklen` print the same integer, with one dependency each and no transformers, PyTorch or ONNX. `JavaScript` `Python`
- **[skills](https://github.com/T0mSIlver/skills)** — the agent skills I run across Claude Code, Codex, opencode and pi: delegating work to another CLI, Remote Control servers under systemd, prose cleanup. Each one is a gotcha backed by evidence, deleted once upstream fixes it. `Shell`

#### Recently in other projects

<!-- recent_contributions starts -->
- ![Open issue](icons/issue_open.svg) [Plugin userConfig options are not expanded in http hook headers (${CLAUDE_PLUGIN_OPTION_*} resolves empty)](https://github.com/anthropics/claude-code/issues/81742) `anthropics/claude-code`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): offer Monthly Plan in the menu bar metric picker](https://github.com/steipete/CodexBar/pull/4072) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): price billing usage by event type, zone, and tier](https://github.com/steipete/CodexBar/pull/4076) `steipete/CodexBar`
- ![Open pull request](icons/pr_open.svg) [Nemotron streaming: compute only new mel frames; keep MLX's buffer cache between steps](https://github.com/Blaizzy/mlx-audio-swift/pull/274) `Blaizzy/mlx-audio-swift`
- ![Draft pull request](icons/pr_draft.svg) [Nemotron streaming: reuse decoder and encoder work that has not changed](https://github.com/Blaizzy/mlx-audio-swift/pull/275) `Blaizzy/mlx-audio-swift`
- ![Merged pull request](icons/pr_merged.svg) [feat(mistral): show the Monthly Plan in widgets](https://github.com/steipete/CodexBar/pull/4038) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): show the Monthly Plan in CLI text output](https://github.com/steipete/CodexBar/pull/4025) `steipete/CodexBar`
- ![Merged pull request](icons/pr_merged.svg) [fix(mistral): allow manual cookies on Linux](https://github.com/steipete/CodexBar/pull/4024) `steipete/CodexBar`
<!-- recent_contributions ends -->

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver) · [PyPI](https://pypi.org/user/T0mSIlver/)
