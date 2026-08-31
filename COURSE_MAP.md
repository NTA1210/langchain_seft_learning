# Course Map — Roadmap Phase 0–42 → Notebooks

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
| 30 | Threat Modeling & Agentic Security Foundations | 16 | OWASP Agentic threat model + risk register |
| 31 | Guardrails & Policy Enforcement | 17 | Policy matrix + deterministic enforcement tests |
| 32 | Identity / Authorization / Tool Security | 18 | Identity model + tool permission matrix |
| 33 | Prompt Injection / Memory / Data Security | 19 | Injection defense + memory-write policy |
| 34 | Sandbox / MCP / Supply Chain Security | 20 | Sandbox design + MCP trust policy + inventory |
| 35 | Agentic Red Teaming / Security Evaluation | 21 | 50+ adversarial cases + security metrics |
| 36 | SecOps / Incident Response | 22 | Alert catalog + kill switch + incident runbook |
| 37 | Reliability / SRE | 23 | Failure taxonomy + SLI/SLO design |
| 38 | Async / Concurrency / Backpressure | 23 | Bounded async execution design |
| 39 | Cost / Latency / Capacity | 23 | Performance and budget benchmark |
| 40 | Deployment / Canary / Rollback | 23 | Deployment and rollback plan |
| 41 | Release Gates / Operational Readiness | 23 | Functional + security eval release gate |
| 42 | Capstone | 23 | Production AI Interview Agent system |

## Graduation artifacts

Kết thúc khóa học, repository của bạn nên có thêm:

```text
artifacts/
├── context-engineering.md
├── rag-benchmark.md
├── evaluation-results.md
├── optimization-report.md
├── security/
│   ├── threat-model.md
│   ├── risk-register.csv
│   ├── policy-matrix.md
│   ├── identity-model.md
│   ├── tool-permission-matrix.md
│   ├── injection-defense.md
│   ├── memory-write-policy.md
│   ├── sandbox-design.md
│   ├── mcp-trust-policy.md
│   ├── supply-chain-inventory.md
│   ├── security-eval-dataset.jsonl
│   ├── security-evaluation-results.md
│   └── incident-response-runbook.md
└── capstone/
    ├── architecture.md
    ├── state-schema.md
    ├── tool-catalog.md
    ├── eval-dataset.jsonl
    ├── runbook.md
    └── README.md
```

Các notebook yêu cầu bạn tự tạo các artifact này; chúng không được pre-fill để tránh biến việc học thành copy/paste.
