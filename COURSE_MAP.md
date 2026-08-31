# Course Map — Roadmap Phase 0–35 → Notebooks

Bảng này bảo đảm toàn bộ roadmap ban đầu đều có chỗ học và output cụ thể.

| Phase | Nội dung | Notebook | Output chính |
|---:|---|---|---|
| 0 | LLM fundamentals | 01 | Raw model mental model + tool-call lifecycle notes |
| 1 | Models | 02 | Provider-independent model wrapper |
| 2 | Messages | 02 | Inspect full message lifecycle |
| 3 | Structured Output | 02 | Pydantic typed extractor |
| 4 | Tools | 03 | Tool library with clear schemas |
| 5 | `create_agent` | 04 | Basic research agent |
| 6 | Streaming | 04 | Token/progress stream |
| 7 | Middleware | 05 | Logging/retry/dynamic behavior |
| 8 | Context Engineering | 05 | Context architecture document |
| 9 | Short-term Memory | 06 | Thread-scoped persistent conversation |
| 10 | Long-term Memory | 06 | User-scoped cross-thread memory |
| 11 | Embeddings | 07 | Semantic search without LLM generation |
| 12 | RAG | 08 | 2-step + agentic + hybrid comparison |
| 13 | LangGraph fundamentals | 09 | Stateful graph |
| 14 | Graph vs Functional API | 09 | Comparison + second implementation exercise |
| 15 | Persistence | 10 | Durable workflow |
| 16 | HITL | 10 | Approval workflow |
| 17 | Time Travel | 10 | Replay/fork exercise |
| 18 | Subgraphs | 10 | Modular graph |
| 19 | Multi-agent | 11 | Router + supervisor patterns |
| 20 | Deep Agents | 12 | Deep research agent |
| 21 | Planning/context offloading | 12 | Long-running plan |
| 22 | Skills | 12 | At least 3 reusable skills |
| 23 | Deep memory | 12 | Persistent agent/user memory design |
| 24 | Subagents | 12 | Specialized subagents |
| 25 | Async subagents | 12 | Preview/advanced investigation |
| 26 | MCP | 13 | Custom MCP server + LangChain client |
| 27 | LangSmith tracing | 14 | Traceable agent |
| 28 | Evaluation | 14 | Dataset + experiment |
| 29 | Agent evaluation | 14 | Tool/trajectory/final-output metrics |
| 30 | Guardrails | 15 | Protected side-effect actions |
| 31 | Security | 15 | Threat model |
| 32 | Async/concurrency | 15 | Async agent path |
| 33 | Cost/latency optimization | 15 | Before/after benchmark |
| 34 | Deployment | 15 | Deployment architecture/checklist |
| 35 | Capstone | 15 | Production-style interview agent system |

## Graduation artifacts

Kết thúc khóa học, repository của bạn nên có thêm:

```text
artifacts/
├── context-engineering.md
├── rag-benchmark.md
├── security-threat-model.md
├── evaluation-results.md
├── optimization-report.md
└── capstone/
    ├── architecture.md
    ├── eval-dataset.jsonl
    └── README.md
```

Các notebook yêu cầu bạn tự tạo các artifact này; chúng không được pre-fill để tránh biến việc học thành copy/paste.
