# 현재 상태와 검증 범위

이 문서는 실제 확보한 기록과 파일을 근거로 작성했습니다. 신규 RAG 구축 결과 보고서가 아닙니다.

| 항목 | 확인 내용 | 근거와 제한 |
|---|---|---|
| 사용자의 사내 환경 | Ollama와 Qwen3:8B로 로컬 LLM을 구현 중이라고 진술 | [2026-10-12 대화](../evidence/codex/01a12f14-af69-7d93-8032-e0303e918e90.md), 원본 L524. 이번 작업에서 사내 PC의 모델 실행을 시험하지 않음 |
| 사내 Langent 설치 | 사용자가 사내 PC에 아직 MCP로 설치되지 않았다고 명시 | 같은 대화 원본 L628. 다른 PC의 과거 설치 기록으로 이 진술을 대체하지 않음 |
| RAG 데이터 정제 | 사용자가 아직 정제 전이라고 명시 | 같은 대화 원본 L628. 정제·인덱싱 완료를 주장하지 않음 |
| 이 작업에서 읽을 수 있는 로컬 개인 플러그인 | `.mcp.json`과 개인 플러그인 manifest 파일 존재. manifest 버전 `0.1.0+codex.20260727092235` | [manifest](../artifacts/langent-plugin/.codex-plugin/plugin.json), [MCP 설정](../artifacts/langent-plugin/.mcp.json). 현재 대화의 Langent 도구 호출 성공을 뜻하지 않음 |
| Langent 도구 정의 | 설치된 `mcp_server.py`에 `langent_ingest`, `langent_query`, `langent_chat`, `langent_graph`, `langent_status`, `langent_nebula` 6개 도구 정의 | [설치본 코드](../evidence/local-runtime/langent/server/mcp_server.py). 도구의 실행 가능 여부·결과 정확성은 이번에 시험하지 않음 |
| Vector DB와 MCP의 역할 | 설치본에 Chroma 벡터 저장소 코드와 MCP 도구 연결 코드가 각각 존재 | [vector.py](../evidence/local-runtime/langent/store/vector.py), [mcp_server.py](../evidence/local-runtime/langent/server/mcp_server.py). 사용자 개인 플러그인과 공개 Windows Kit의 문서를 구분해야 함 |
| Langent의 Qwen3 연결 | 수집한 설치본의 Ollama 요청 payload에는 `model: llama3`가 명시되어 있음 | [llm_proxy.py](../evidence/local-runtime/langent/llm_proxy.py). 이 파일로 Qwen3:8B 연결 완료를 주장할 수 없음 |
| 기존 Hue RAG 저장소 | TypeSafe 후보 문서 판정 코드와 Chroma 파일 존재 | [실제 코드](../artifacts/01_vector_db/src/typesafe_rag_gate.py), [기존 README](../artifacts/01_vector_db/README.md). 판정 코드는 검색·답변 생성 자체를 담당하지 않는다고 명시 |
| 수집한 벡터 파일의 구조 | 두 보관 SQLite 파일 각각 `embeddings` 테이블 27행, `langent_knowledge` 컬렉션 차원 384, `quick_check: ok` | [사본 검사 결과](../evidence/sqlite-checks.json). 검색 품질·HNSW 동작·전체 서비스 복원 시험을 의미하지 않음 |
| 과거 KNCCS 그래프 생성 | 기존 보고서에 `vector_count: 834`, `semantic_entities: 22`, `semantic_relations: 26`, `chunk_entity_mentions: 763`, `neo4j_connected: true` 기록 | [원본 보고서](../artifacts/knccs-graph/knowledge_graph_report.json), [당시 대화](../evidence/codex/019fa65e-55be-76d0-84d8-f85bef24ffe2.md). 과거 보고서의 값이며 현재 Neo4j 상태를 재측정한 값이 아님 |
| GraphRAG 전체 흐름 | 과거 응답에는 완료 선언이 있으나, 이번 확보 자료만으로 그래프 검색 근거가 실제 최종 답변에 사용되는 전체 흐름을 인증하지 않음 | 위 보고서와 코드·대화만 보존. 그래프 생성, 검색, 답변 생성, 출처 검증의 각 실행 증거는 구분해야 함 |
| Dify | 현재 대화에서 신규 RAG 관리 도구의 선택지로 제안됨 | [2026-10-12 대화](../evidence/codex/01a12f14-af69-7d93-8032-e0303e918e90.md). 설치·배포·연결 완료 기록으로 바꾸지 않음 |
| 원격 사용과 권한 | ChatGPT의 RAG PoC 기록은 실제 원격 RAG·권한 검증이 미완료라고 명시 | [RAG 구축 순서 화면](../evidence/chatgpt/rag-sequence-conversation.snapshot.txt), [원격 접속 기록](../evidence/chatgpt/local-llm-firewall.snapshot.txt). 제시된 시험 절차를 성공 결과로 바꾸지 않음 |

## 서로 다른 기록을 해석하는 방법

2026년 6월·7월 개인 환경에서의 Langent 설치·갱신 기록과 10월의 사내 PC 미설치 진술은 환경과 시점이 다릅니다. 이 저장소에서는 둘을 하나의 배포 상태로 합치지 않았습니다.

공개 One-Click Kit의 README만으로 개인 Codex 플러그인의 기능을 확정할 수 없습니다. 이번에 확보한 개인 플러그인 manifest와 설치본 MCP 코드를 함께 보존했습니다.

## 앞으로 확인이 필요한 작업

아래는 기존 요청과 대화에 나온 미완료 항목입니다. 이번 등록 작업에서 구현한 기능이 아닙니다.

- 승인본·최신 버전·중복 문서·원문 위치·열람 권한을 정리한 시범 자료 준비
- 사내 환경에서 사용할 RAG 도구와 임베딩 모델의 실제 연결 확인
- 검색된 원문과 답변의 출처 대조, 근거가 없는 질문의 응답 제한 확인
- 사용자별 문서 권한, 삭제·권한 변경 반영, 원격 접속의 실제 시험
- GraphRAG 적용 시 그래프 검색 결과가 최종 답변에 사용되는지 실행 기록 확보

저비용·간편 구축·할루시네이션 최소화는 사용자의 목표입니다. 이 자료에서 실제 비용, 구축 시간 또는 환각 감소율의 실측 결과는 확보하지 않았습니다.
