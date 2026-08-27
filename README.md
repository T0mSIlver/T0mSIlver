### Tom Vaucourt

AI engineer — Local inference and agentic developer tooling. I build end-to-end systems and contribute upstream to the tools I depend on.

**Now:** [vidtheque](https://github.com/T0mSIlver/vidtheque), a self-hosted video knowledge base your coding agent can query mid-task, live at [vidtheque.dev](https://vidtheque.dev). Still shipping voice for coding agents in [localvoxtral](https://github.com/T0mSIlver/localvoxtral).

#### Selected work

- **[vidtheque](https://github.com/T0mSIlver/vidtheque)** — the talks you don't have time to watch, turned into knowledge an agent can query. Word-level transcripts, OCR of what crossed the screen, embedded keyframes, served over MCP, and every answer carries its receipt: the sentence, the slide, and the second it happened (`youtu.be/ID?t=123`). Two services, HTTP between them: a CPU process that runs on a Pi holds the index and the dashboards, a stateless GPU worker does STT/OCR/embeddings behind OpenAI-shaped endpoints. One model, `Qwen3-VL-Embedding-2B`, reads a slide as a document rather than a picture. The [public demo](https://vidtheque.dev/demo) is all 310 AI Engineer 2026 talks: 107 hours, 69k transcript cues, 13k keyframes. MIT, ships as images. `Python` `JavaScript`
- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)** — native macOS menu-bar app for realtime, fully local dictation: words appear while you're still speaking. Built first for prompting coding agents by voice, so it joins the *exact* Claude Code session under your cursor — Ghostty, iTerm2, Terminal.app, a [herdr](https://herdr.dev) or cmux pane, over SSH, or a claude.ai/code tab — and grounds LLM polishing in that session's screen, last prompt, and repo vocabulary. Runs Mistral's Voxtral Mini 4B Realtime on Apple Silicon, or any OpenAI Realtime-compatible backend. `Swift`
- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)** — contributor to the Voxtral realtime streaming path: incremental mel/conv front end (O(N²) → O(N) per utterance), fp16 dtype fixes, Metal buffer-pool policy, and quantized tied-embedding loading — teaching the engine to load a [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) I publish, which cuts the per-token LM-head projection ~10× (~30 ms → ~3 ms on an M1 Pro). Streaming went from ~1.9× slower than realtime to a flat 0.76 RTF. `Swift`
- **[working-set](https://github.com/T0mSIlver/working-set)** — how many agents a given GPU configuration can keep warm, and which constraint binds first: KV cache, decode bandwidth, or prefill compute. A scenario model in Python and a dependency-free [interactive explorer](https://workingset.tomvaucourt.com/) that answers as a decision tool — binding-constraint verdict, vLLM flags, the electricity bill, and the assumption that would flip the call. It also generates the load-test script to check its own predictions against a live endpoint. `Python` `HTML`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)** — merged: preserve Anthropic thinking blocks through the server's message conversion. `C++`
- **[fastcontext](https://github.com/T0mSIlver/fastcontext)** — read-only repository-exploration agent that coding agents delegate to over bash: cited `file:line` answers, not context noise. `Python`
- **[toklen](https://github.com/T0mSIlver/toklen)** — count tokens with a model's real Hugging Face tokenizer. `npx toklen` and `uvx toklen` print the same integer; one dependency each, no transformers, no PyTorch, no ONNX. `JavaScript` `Python`
- **[voxmlx](https://github.com/T0mSIlver/voxmlx)** — realtime Voxtral transcription in MLX; my fork adds an OpenAI-Realtime-compatible WebSocket server and Metal memory caps. 4-bit conversions on [Hugging Face](https://huggingface.co/T0mSIlver). `Python`
- **[pi-intl-segmenter-fallback](https://www.npmjs.com/package/pi-intl-segmenter-fallback)** — diagnosed a V8 segfault (null `icu::BreakIterator` on small-ICU Node builds, [nodejs/node#51752](https://github.com/nodejs/node/issues/51752)), filed it upstream with a proposed patch, and shipped this pure-JS `Intl.Segmenter` fallback to npm the same day. `TypeScript`
- **[pi-llamacpp-provider](https://github.com/T0mSIlver/pi-llamacpp-provider)** — pi extension that registers a llama.cpp server as a provider and auto-discovers every model it exposes. `JavaScript`
- **[skills](https://github.com/T0mSIlver/skills)** — skills that let a coding agent delegate work to another coding CLI and keep itself in sync from git. `Shell`

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

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver)
