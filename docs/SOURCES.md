# 근거 목록

이 문서의 기술적 내용은 확보한 원문과 파일에서 확인합니다. 외부 제품의 최신 기능·가격·성능을 이번 보관 작업에서 새로 검증한 것은 아닙니다.

## 로컬 Codex 기록

[세션별 manifest](../evidence/codex/manifest.json)에 원본 로그 경로, 줄 번호, 시간과 SHA-256을 기록했습니다. 역할이 표시된 대화 발췌는 원본 발언 기록이며, assistant 응답을 자동으로 검증된 사실로 승격하지 않습니다.

## 로그인된 ChatGPT 기록

| 원문 제목 | 원문 URL | 보존본 |
|---|---|---|
| RAG 구축 순서와 내용 | [원문](https://chatgpt.com/g/g-p-6ab1ec90d2048191923833b6b5d8b71e-llm-gucug/c/6acb4c40-c3fc-83e8-b13d-ed3c4da12059) | [스냅샷](../evidence/chatgpt/rag-sequence-conversation.snapshot.txt) |
| 프롬프트 개선 RAG 구축 | [원문](https://chatgpt.com/g/g-5XtVuRE8Y-prompt-engineer/c/6accb06a-5e54-83ee-a5a8-22583abb5e60) | [스냅샷](../evidence/chatgpt/enterprise-rag-prompt.snapshot.txt) |
| 로컬 LLM 구축안 | [원문](https://chatgpt.com/g/g-p-6ab1ec90d2048191923833b6b5d8b71e-llm-gucug/c/6ab1ed12-93d8-83e8-87e5-be5fd71e8e53) | [스냅샷](../evidence/chatgpt/local-llm.snapshot.txt) |
| 파인튜닝과 데이터 우선순위 | [원문](https://chatgpt.com/g/g-p-6ab1ec90d2048191923833b6b5d8b71e-llm-gucug/c/6acc7ec3-3e74-83ec-80e4-404f100cd803) | [스냅샷](../evidence/chatgpt/fine-tuning-data.snapshot.txt) |
| 원격 데스크톱 방화벽 재차단 확인 | [원문](https://chatgpt.com/g/g-p-6ab1ec90d2048191923833b6b5d8b71e-llm-gucug/c/6accb3b9-9710-83ee-9f95-55ff29a15095) | [스냅샷](../evidence/chatgpt/local-llm-firewall.snapshot.txt) |
| 온톨로지 팩 추천: 문서 근거 관리 참고 | [원문](https://chatgpt.com/g/g-p-6a8bdd53f23881919b420b0a0cf4234c-suculibeunhaeng/c/6acc7171-2f88-83e8-b1c6-674012f68f9a) | [스냅샷](../evidence/chatgpt/ontology-pack-recommendation.snapshot.txt) |
| 온톨로지 팩 제공 request | [원문](https://chatgpt.com/g/g-p-6ab1ec90d2048191923833b6b5d8b71e-llm-gucug/c/6acc43f1-7284-83ee-9b5d-fb5e68ab5142) | [스냅샷](../evidence/chatgpt/ontology-pack-request.snapshot.txt) |
| 온톨로지 팩 조회 | [원문](https://chatgpt.com/g/g-p-6a9cf8a9ff948191b51efc1190cab3f6-jagigyebal/c/6acb24ef-edd0-83e8-a494-a1cbf7b82517) | [스냅샷](../evidence/chatgpt/ontology-pack-list.snapshot.txt) |
| 오픈크랩 팩 추천 | [원문](https://chatgpt.com/c/6acb14cb-58cc-83ee-93ab-872e231e95ee) | [스냅샷](../evidence/chatgpt/opencrab-rag-packs.snapshot.txt) |
| 남진 AI 자동화와 Graph RAG 사이트 | [원문](https://namjin-ai-systems.namjini.chatgpt.site/) | [스냅샷](../evidence/chatgpt/ai-graphrag-site-authenticated.snapshot.txt) |

## 실제 파일

- [기존 저장소 기준 커밋](https://github.com/namjincool/01_vector_db/tree/060dceb9a9ea7cb2ffff8e09edefd7a4d28aec59) 및 [GitHub 수집 메타데이터](../evidence/source-repository.json)
- [TypeSafe RAG 후보 판정 코드](../artifacts/01_vector_db/src/typesafe_rag_gate.py)
- [개인 Langent 플러그인 manifest](../artifacts/langent-plugin/.codex-plugin/plugin.json) 및 [MCP 설정](../artifacts/langent-plugin/.mcp.json)
- [실제 설치본의 MCP 서버 코드](../evidence/local-runtime/langent/server/mcp_server.py)
- [기존 KNCCS 그래프 보고서](../artifacts/knccs-graph/knowledge_graph_report.json), [생성 코드](../artifacts/knccs-graph/build_knccs_knowledge_graph.py)
- [기존 KNCCS SVG](../artifacts/knccs-graph/KNCCS_GraphRAG_Ontology.svg), [ChatGPT 라이브러리 원본](https://chatgpt.com/library/file/libfile_19886e9567008191b0c57e30a6b78075)
- [기존 RAG 사이트 제공 HTML](../artifacts/namjin-ai-site/served.html)
- [사용자 첨부 프롬프트](../prompts/enterprise-rag-user-prompt.txt)

## 기존 대화에서 참조한 공개 원문

- [공개 Windows Kit](https://github.com/sodam-ai/Langent-MCP_One-Click_Kit)
- [Langent 본체](https://github.com/AlexAI-MCP/langent)
- [Dify 공식 문서](https://docs.dify.ai/)
- [Ollama 공식 문서](https://docs.ollama.com/)

구체적 문서 URL은 보존한 Codex 응답에 원문대로 남아 있습니다. URL의 존재나 과거 답변 인용만으로 현재 제품 지원·성능·요금을 보증하지 않습니다.
