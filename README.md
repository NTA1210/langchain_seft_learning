# Langchain_Advanced — Production-First Learning Path

Chương trình tự học LangChain ecosystem từ nền tảng LLM đến production agent systems.

> **Baseline cập nhật:** 2026-09. Course ưu tiên LangChain v1+, LangGraph v1+, Deep Agents, LangSmith và MCP. Các API legacy như `LLMChain`, `ConversationChain`, `AgentExecutor` và `langgraph.prebuilt.create_react_agent` chỉ được nhắc để nhận diện code cũ, không dùng làm learning path chính.

## Mục tiêu cuối khóa

Sau khi hoàn thành, bạn phải có khả năng nhìn một requirement và quyết định:

1. Có thật sự cần agent không?
2. Cần tool calling, structured output hay workflow deterministic?
3. Cần short-term hay long-term memory?
4. RAG nên dùng 2-step, agentic hay hybrid?
5. Khi nào dùng LangChain, LangGraph, Deep Agents?
6. Single-agent có đủ không hay cần multi-agent?
7. Human approval cần đặt ở đâu?
8. Context nào model được thấy ở từng bước?
9. Đánh giá quality bằng metric nào?
10. Làm sao deploy, trace, secure và tối ưu cost/latency?

## Provider strategy cho khóa học

Mặc định course **không yêu cầu OpenAI/Anthropic trả phí**.

| Priority | Provider | Vai trò trong course | Ghi chú |
|---|---|---|---|
| 1 | Gemini Developer API | Provider mặc định | Dễ setup, hỗ trợ tool calling, structured output, streaming, async và embeddings |
| 2 | Groq | Provider phụ | Tốc độ cao, phù hợp test agent/tool calling |
| 3 | OpenRouter | Fallback | Dùng `openrouter/free` hoặc model `:free`; quota/availability có thể thay đổi |
| 4 | Ollama | Local/offline | Không tốn API nhưng cần máy đủ RAM/VRAM |

**Ngrok không phải LLM provider.** Ngrok là tunneling/reverse-proxy tool. Nó chỉ hữu ích ở các phần MCP/deployment khi cần expose local server ra Internet.

Model IDs và free-tier quota thay đổi theo thời gian, vì vậy toàn bộ notebooks đọc model từ `.env` thay vì hard-code business logic.

## Setup nhanh

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
jupyter lab
```

Điền ít nhất một API key vào `.env`:

```env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=...
```

## Cấu trúc course

```text
Langchain_Advanced/
├── README.md
├── COURSE_MAP.md
├── requirements.txt
├── .env.example
├── src/
│   └── providers.py
└── notebooks/
    ├── 00_setup/
    ├── 01_fundamentals/
    ├── 02_langchain_core/
    ├── 03_agents/
    ├── 04_context_memory/
    ├── 05_rag/
    ├── 06_langgraph/
    ├── 07_multi_agent/
    ├── 08_deep_agents/
    ├── 09_mcp_langsmith/
    ├── 10_security/
    └── 11_production_capstone/
```

## Quy tắc học

Mỗi notebook đều có 5 phần:

1. **Learning requirements** — phải hiểu gì.
2. **Concepts** — giải thích kiến thức.
3. **Lab** — code chạy được hoặc scaffold có TODO rõ.
4. **Required output** — artifact phải tạo.
5. **Done criteria** — điều kiện để được chuyển sang bài tiếp theo.

Không chỉ chạy notebook rồi xem như hoàn thành. Hãy sửa TODO, thử input khác, cố tình tạo lỗi và ghi lại observation.

## Security level

Security không còn là một checklist ở notebook cuối. Course có một level riêng gồm:

- threat modeling theo OWASP Agentic Top 10 2026;
- guardrails + deterministic policy enforcement;
- identity, authorization và least privilege cho tools;
- prompt injection, memory poisoning và data isolation;
- sandbox, MCP và agentic supply-chain security;
- adversarial/security evaluation;
- SecOps, kill switch và incident response.

Security labs dùng fixtures/simulations trong controlled environment. Mục tiêu là xây **defensive controls + measurable security tests**.

Graduation flow:

```text
Agent Engineering -> Evaluation -> AI Agent Security -> Reliability/SRE -> Capstone
```

## Recommended order

1. `00_setup/00_environment_and_providers.ipynb`
2. `01_fundamentals/01_llm_and_tool_calling_fundamentals.ipynb`
3. `02_langchain_core/02_models_messages_structured_output.ipynb`
4. `02_langchain_core/03_tools_runtime.ipynb`
5. `03_agents/04_agent_loop_create_agent_streaming.ipynb`
6. `03_agents/05_middleware_context_engineering.ipynb`
7. `04_context_memory/06_memory.ipynb`
8. `05_rag/07_embeddings_semantic_search.ipynb`
9. `05_rag/08_rag_architectures.ipynb`
10. `06_langgraph/09_langgraph_fundamentals.ipynb`
11. `06_langgraph/10_langgraph_advanced.ipynb`
12. `07_multi_agent/11_multi_agent_patterns.ipynb`
13. `08_deep_agents/12_deep_agents.ipynb`
14. `09_mcp_langsmith/13_mcp.ipynb`
15. `09_mcp_langsmith/14_langsmith_observability_evaluation.ipynb`
16. `10_security/16_ai_security_foundations.ipynb`
17. `10_security/17_guardrails_policy_enforcement.ipynb`
18. `10_security/18_identity_authorization_tool_security.ipynb`
19. `10_security/19_prompt_injection_memory_data_security.ipynb`
20. `10_security/20_sandbox_mcp_supply_chain_security.ipynb`
21. `10_security/21_agentic_red_teaming_security_eval.ipynb`
22. `10_security/22_agent_secops_incident_response.ipynb`
23. `11_production_capstone/23_production_reliability_and_capstone.ipynb`

Chi tiết mapping toàn bộ roadmap từ **Phase 0 đến Phase 42** nằm trong [COURSE_MAP.md](COURSE_MAP.md).

## Legacy warning

Khi gặp tutorial cũ, hãy kiểm tra kỹ nếu thấy:

- `LLMChain`
- `ConversationChain`
- `AgentExecutor`
- `langgraph.prebuilt.create_react_agent`
- code dựa trên `langchain-classic`

Bạn vẫn nên biết chúng tồn tại để maintain project cũ, nhưng không dùng chúng làm trục chính cho project mới.

## Capstone

Capstone của course là **AI Interview Agent / Codebase Interview System** có:

- source-code scanning,
- RAG,
- structured interview state,
- dynamic questions,
- LangGraph workflow,
- persistence + resume,
- human-in-the-loop,
- specialized subagents,
- MCP tools,
- LangSmith tracing/evaluation,
- threat model,
- deterministic authorization + guardrails,
- prompt-injection/memory-poison defenses,
- sandbox/MCP/supply-chain controls,
- security regression evaluation,
- kill switch + incident response,
- streaming,
- reliability/SRE,
- canary/rollback + release gates.

Chi tiết nằm trong notebook cuối.
