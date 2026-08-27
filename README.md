### Tom Vaucourt

AI engineer — Local inference and agentic developer tooling. I build end-to-end systems and contribute upstream to the tools I depend on.

**Now:** [vidtheque](https://github.com/T0mSIlver/vidtheque), a self-hosted video knowledge base your coding agent can query mid-task, live at [vidtheque.dev](https://vidtheque.dev). Still shipping voice for coding agents in [localvoxtral](https://github.com/T0mSIlver/localvoxtral).

#### Selected work

- **[vidtheque](https://github.com/T0mSIlver/vidtheque)** — the talks you don't have time to watch, turned into knowledge an agent can query over MCP. Word-level transcripts, on-screen text, keyframes, and every answer carries its receipt: the sentence, the slide, and the second it happened. Self-hosted; the [demo](https://vidtheque.dev/demo) indexes 310 AI Engineer talks. `Python` `JavaScript`
- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)** — native macOS menu-bar app for realtime, fully local dictation: words appear while you're still speaking. Built for prompting coding agents by voice, so it joins the exact Claude Code session under your cursor and grounds LLM polishing in its screen and repo vocabulary. `Swift`
- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)** — contributor to the Voxtral realtime streaming path: incremental mel/conv front end (O(N²) → O(N) per utterance), fp16 fixes, Metal buffer-pool policy, and loading the [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) I publish. Streaming went from ~1.9× slower than realtime to a flat 0.76 RTF. `Swift`
- **[working-set](https://github.com/T0mSIlver/working-set)** — how many agents a given GPU configuration keeps warm, and which constraint binds first: KV cache, decode bandwidth, or prefill compute. A scenario model and an [explorer](https://workingset.tomvaucourt.com/) that answers with a verdict, the vLLM flags, and the assumption that would flip the call. `Python` `HTML`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)** — merged: preserve Anthropic thinking blocks through the server's message conversion. `C++`
- **[fastcontext](https://github.com/T0mSIlver/fastcontext)** — read-only repository-exploration agent that coding agents delegate to over bash: cited `file:line` answers, not context noise. `Python`
- **[toklen](https://github.com/T0mSIlver/toklen)** — count tokens with a model's real Hugging Face tokenizer. `npx toklen` and `uvx toklen` print the same integer; one dependency each, no transformers, no PyTorch, no ONNX. `JavaScript` `Python`
- **[skills](https://github.com/T0mSIlver/skills)** — Agent Skills that let a coding agent drive another coding CLI without losing control of the main checkout: reviewer and edit-worker profiles for `claude`, `codex` and `opencode`, a live codex pane over [herdr](https://herdr.dev), and per-repo Remote Control servers under systemd. Vendored copies stay pristine, tracked by a daily update PR. `Shell`

#### Recently in other projects

<!-- recent_contributions starts -->
- ![Open issue](icons/issue_open.svg) [Plugin userConfig options are not expanded in http hook headers (${CLAUDE_PLUGIN_OPTION_*} resolves empty)](https://github.com/anthropics/claude-code/issues/81742) `anthropics/claude-code`
- ![Closed issue](icons/issue_closed.svg) [Prompt-cache reuse can return KV state that doesn't match the keyed prefix (windowed-cache trim contract)](https://github.com/ml-explore/mlx-lm/issues/1494) `ml-explore/mlx-lm`
- ![Closed issue](icons/issue_closed.svg) [LRUPromptCache: one-token prefixes never match in PromptTrie.search; eviction ignores fetch recency (FIFO, not LRU)](https://github.com/ml-explore/mlx-lm/issues/1495) `ml-explore/mlx-lm`
- ![Closed pull request](icons/pr_closed.svg) [Fix LRUPromptCache: return one-token prefix matches and refresh LRU recency on fetch](https://github.com/ml-explore/mlx-lm/pull/1496) `ml-explore/mlx-lm`
- ![Closed pull request](icons/pr_closed.svg) [Prompt cache: never reuse KV that fails to trim to the keyed prefix](https://github.com/ml-explore/mlx-lm/pull/1502) `ml-explore/mlx-lm`
- ![Closed pull request](icons/pr_closed.svg) [Prompt cache: don't reuse a slid windowed cache as a keyed prefix](https://github.com/ml-explore/mlx-lm/pull/1503) `ml-explore/mlx-lm`
- ![Closed pull request](icons/pr_closed.svg) [.NET: Add SuppressAssistantName option to ChatClientAgentOptions](https://github.com/microsoft/agent-framework/pull/1822) `microsoft/agent-framework`
- ![Answered discussion](icons/discussion_answered.svg) [Docs: "against independent benchmarks" link is dead (TechEmpower benchmarks site)](https://github.com/Kludex/starlette/discussions/3433) `Kludex/starlette`
<!-- recent_contributions ends -->

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver) · [PyPI](https://pypi.org/user/T0mSIlver/)
