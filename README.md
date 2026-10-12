# RAG · Langent 작업 기록

2026-10-12까지 접근 가능한 RAG·Langent 관련 작업의 근거 보관 저장소입니다. 사용자가 요청한 범위에 맞춰 현재 대화, 다른 로컬 Codex 세션, 로그인된 ChatGPT 기록, 기존 파일 및 GitHub 저장소를 확인했습니다.

이 저장소의 문서 정리는 이번 등록 작업에서 작성했습니다. 과거 작업의 구현 여부는 원본 기록과 파일로 판단하며, 과거 assistant의 완료 선언만으로 구현 완료를 인정하지 않습니다.

## 먼저 읽을 자료

- [현재 상태와 검증 범위](docs/STATUS.md)
- [날짜별 작업 기록](docs/WORKLOG.md)
- [수집 범위와 누락·제외 기록](docs/COVERAGE.md)
- [근거 목록](docs/SOURCES.md)
- [사용자가 업로드한 Enterprise RAG 프롬프트 원문](prompts/enterprise-rag-user-prompt.txt)

## 보존한 자료

| 위치 | 내용 |
|---|---|
| `evidence/codex/` | 관련 Codex 세션 15개, user/assistant 메시지 92개. 원본 로그 줄 번호·시간·해시 포함 |
| `evidence/chatgpt/` | 로그인된 ChatGPT에서 확인한 관련 대화 본문, 검색 결과, 사이트 접근 상태 |
| `artifacts/01_vector_db/` | 기존 저장소의 실제 코드, RAG 소스 문서, PDF 및 Chroma 파일 |
| `artifacts/langent-plugin/` | 기존 개인 플러그인의 manifest, MCP 설정, 설치 스크립트 및 문서 |
| `artifacts/knccs-graph/` | 기존 문서 추출본, 그래프 생성 코드, 결과 보고서, ChatGPT의 기존 SVG |
| `artifacts/namjin-ai-site/` | 사용자 승인 로그인 후 읽은 기존 RAG 사이트의 실제 제공 HTML |
| `artifacts/langent-runtime-data/` | 기존 로컬 런타임의 벡터 데이터 파일 사본 |
| `evidence/local-runtime/` | 실제 설치 경로에서 읽은 Langent 코드 일부와 라이선스 |
| `evidence/artifact-manifest.json` | 파일별 출처·원본/보존본 SHA-256·크기 |

기존 `01_vector_db`의 기준 커밋은 `060dceb9a9ea7cb2ffff8e09edefd7a4d28aec59`입니다. 해당 저장소의 자료는 Git 체크아웃에서 읽은 파일 바이트를 보존했습니다.

## 기록 해석 원칙

1. **사용자 진술**: 사용자가 설명한 환경과 목표. PC에서 직접 실행해 검증한 사실과 구분합니다.
2. **대화 기록**: 당시 질문·답변·제안의 원문. 답변 자체의 정확성을 새로 보증하는 자료는 아닙니다.
3. **파일 확인**: 실제 존재하는 설정·코드·보고서·데이터를 수집한 사실. 해당 서비스의 현재 정상 실행을 뜻하지 않습니다.
4. **미검증**: 실행 로그, 검색 경로, 원문 대조 또는 권한 시험이 확보되지 않은 항목. 완료 상태를 만들지 않습니다.

ChatGPT 자료는 웹 화면에서 접근 가능한 내용의 스냅샷입니다. 계정 전체 데이터 내보내기 파일은 아니며, 숨겨진 메시지·생성 UI의 일부 표/코드·삭제된 기록의 완전성을 보장하지 않습니다. 범위와 제한은 [COVERAGE](docs/COVERAGE.md)에 기록했습니다.
