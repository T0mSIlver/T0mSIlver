### Tom Vaucourt

AI engineer — Local inference and agentic developer tooling. I build end-to-end systems and contribute upstream to the tools I depend on.

**Now:** on-device speech for Apple Silicon — shipping [localvoxtral](https://github.com/T0mSIlver/localvoxtral) and contributing the Voxtral realtime inference path to [mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift).

#### Selected work

- **[localvoxtral](https://github.com/T0mSIlver/localvoxtral)** — native macOS menu-bar app for realtime, fully local dictation: words appear while you're still speaking, with optional on-device LLM polishing. Runs Mistral's Voxtral Mini 4B Realtime on Apple Silicon, or against any OpenAI Realtime-compatible backend. `Swift`
- **[mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift/pulls?q=is%3Apr+author%3AT0mSIlver)** — contributor to the Voxtral realtime streaming path: incremental mel/conv front end (O(N²) → O(N) per utterance), fp16 dtype fixes, Metal buffer-pool policy, and quantized tied-embedding loading — teaching the engine to load a [4-bit tied-head checkpoint](https://huggingface.co/T0mSIlver/Voxtral-Mini-4B-Realtime-2602-4bit-qhead) I publish, which cuts the per-token LM-head projection ~10× (~30 ms → ~3 ms on an M1 Pro). Streaming went from ~1.9× slower than realtime to a flat 0.76 RTF. `Swift`
- **[llama.cpp #20120](https://github.com/ggml-org/llama.cpp/pull/20120)** — merged: preserve Anthropic thinking blocks through the server's message conversion. `C++`
- **[fastcontext](https://github.com/T0mSIlver/fastcontext)** — read-only repository-exploration agent that coding agents delegate to over bash: cited `file:line` answers, not context noise. `Python`
- **[voxmlx](https://github.com/T0mSIlver/voxmlx)** — realtime Voxtral transcription in MLX; my fork adds an OpenAI-Realtime-compatible WebSocket server and Metal memory caps. 4-bit conversions on [Hugging Face](https://huggingface.co/T0mSIlver). `Python`
- **[pi-intl-segmenter-fallback](https://www.npmjs.com/package/pi-intl-segmenter-fallback)** — diagnosed a V8 segfault (null `icu::BreakIterator` on small-ICU Node builds, [nodejs/node#51752](https://github.com/nodejs/node/issues/51752)), filed it upstream with a proposed patch, and shipped this pure-JS `Intl.Segmenter` fallback to npm the same day. `TypeScript`
- **[pi-llamacpp-provider](https://github.com/T0mSIlver/pi-llamacpp-provider)** — pi extension that registers a llama.cpp server as a provider and auto-discovers every model it exposes. `JavaScript`
- **[skills](https://github.com/T0mSIlver/skills)** — skills that let a coding agent delegate work to another coding CLI and keep itself in sync from git. `Shell`

#### Recently in other projects

<!-- recent_contributions starts -->
- **open issue** [Plugin userConfig options are not expanded in http hook headers (${CLAUDE_PLUGIN_OPTION_*} resolves empty)](https://github.com/anthropics/claude-code/issues/81742) — [anthropics/claude-code](https://github.com/anthropics/claude-code)
- **open issue** [Hosting: llama.cpp needs `--reasoning-format none`](https://github.com/microsoft/fara/issues/82) — [microsoft/fara](https://github.com/microsoft/fara)
- **open issue** [Recovered daemon-transport bounce leaves a permanent error on the workspace row](https://github.com/manaflow-ai/cmux/issues/8917) — [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)
- **merged** [VoxtralRealtime: load checkpoints with a quantized tied embedding](https://github.com/Blaizzy/mlx-audio-swift/pull/232) — [Blaizzy/mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift)
- **merged** [Hoist per-layer-invariant attention inputs out of the Voxtral layer loops](https://github.com/Blaizzy/mlx-audio-swift/pull/231) — [Blaizzy/mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift)
- **merged** [VoxtralRealtime streaming: stop clearing the Metal buffer pool on every step](https://github.com/Blaizzy/mlx-audio-swift/pull/229) — [Blaizzy/mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift)
- **merged** [VoxtralRealtime streaming: incremental mel/conv front end (O(N²) → O(N) per utterance)](https://github.com/Blaizzy/mlx-audio-swift/pull/230) — [Blaizzy/mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift)
- **merged** [Fix float32 leak in VoxtralRealtime streaming](https://github.com/Blaizzy/mlx-audio-swift/pull/226) — [Blaizzy/mlx-audio-swift](https://github.com/Blaizzy/mlx-audio-swift)
<!-- recent_contributions ends -->

<sub>Updated daily by [`build_readme.py`](build_readme.py).</sub>

#### Elsewhere

[LinkedIn](https://www.linkedin.com/in/tomvaucourt/) · [Hugging Face](https://huggingface.co/T0mSIlver) · [npm](https://www.npmjs.com/~t0msilver)
