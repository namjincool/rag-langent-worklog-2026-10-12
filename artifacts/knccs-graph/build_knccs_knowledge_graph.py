import json
from pathlib import Path

from langent.brain import Langent


DOCUMENT_NAME = "(′26년 KNCCS 노후 네트워크장비 교체사업) 정성제안서_원본_1권.md"
PROJECT_NAME = "′26년 KNCCS 노후 네트워크장비 교체사업"
REPORT_PATH = Path(
    r"C:\Users\허남진_N01\Desktop\허남진\01_개인\공부 및 자료\ppt_convert"
    r"\langent_ingest\knccs_2026_qualitative_proposal_vol1\knowledge_graph_report.json"
)


ENTITIES = [
    ("Project", PROJECT_NAME, "KNCCS 노후 네트워크 장비를 무중단으로 교체하는 사업", [PROJECT_NAME, "KNCCS"]),
    ("Goal", "무중단 운용 보장", "교체 중 KNCCS 업무 연속성 유지", ["무중단", "업무 연속성"]),
    ("Goal", "완전 호환 및 연동", "기 운용 체계와 신규 장비의 호환성·연동성 보장", ["호환성", "연동성", "설정이관"]),
    ("Goal", "보안 완결성", "군 보안 기준과 보안 적합성 요구 충족", ["보안기능확인서", "보안취약", "군사보안"]),
    ("Goal", "일정 준수", "단납기·전국 분산 구축 일정 준수", ["일정 준수", "일정지연", "공정"]),
    ("Equipment", "백본스위치", "교체 대상 핵심 네트워크 장비 18대", ["백본스위치"]),
    ("Equipment", "L4스위치", "교체 대상 핵심 네트워크 장비 28대", ["L4스위치", "L4 스위치"]),
    ("Scope", "9개 대상 부대", "전국 9개 부대 대상 분산 구축", ["9개 부대", "사업대상부대"]),
    ("Strategy", "무중단 순차 교체", "부대별 순차 교체로 서비스 중단 최소화", ["순차적인 장비 교체", "무중단 교체"]),
    ("Strategy", "현황 실사 및 사전 협의", "부대별 현황·일정을 사전 조사하고 공유", ["현황 실사", "사전 협의"]),
    ("Strategy", "설정 이관 및 연동", "기존 설정을 이관하고 운용 체계와 연동", ["설정이관", "설정 이관", "연동"]),
    ("Strategy", "부대별 인수시험", "설치 후 부대 단위 인수시험 수행", ["인수시험"]),
    ("Strategy", "권역별 전담조직", "동해권·남해권·서해권 전담조직 운영", ["동해권", "남해권", "서해권"]),
    ("Strategy", "취약점 전수조치", "보안 취약점을 전수 점검·조치한 뒤 구축", ["취약점전수조치", "취약점 분석"]),
    ("Strategy", "일정 모니터링 및 예비자원 투입", "진도 모니터링과 예비 인력 투입으로 지연 만회", ["진행상태 모니터링", "예비 자원", "일정지연"]),
    ("Requirement", "보안기능확인서", "도입 장비의 보안 적합성 입증", ["보안기능확인서"]),
    ("Requirement", "10년 부품·기술지원", "장기 운용을 위한 제조사 지원 확약", ["10년부품", "기술지원확약"]),
    ("Requirement", "ISO 45001 기반 안전관리", "국제표준 기반 현장 안전관리", ["ISO45001", "ISO 45001"]),
    ("Outcome", "KNCCS 운용 안정성 향상", "노후 장비 교체와 무중단 구축을 통한 안정성 강화", ["운용안정성", "체계의 안정성"]),
    ("Outcome", "고가용 네트워크 환경", "해군 전술 C4I 체계의 고가용 운용 환경", ["고가용", "고가용성"]),
    ("Outcome", "해군 작전지휘통제 능력 강화", "안정적인 KNCCS 운용을 통한 작전 역량 강화", ["작전지휘통제 능력강화", "작전지휘통제"]),
    ("Outcome", "장기 운용 보장", "부품과 기술지원 확보를 통한 장기 운영", ["장기운용보장", "장기 운용"]),
]


RELATIONS = [
    ("Project", PROJECT_NAME, "HAS_GOAL", "Goal", "무중단 운용 보장"),
    ("Project", PROJECT_NAME, "HAS_GOAL", "Goal", "완전 호환 및 연동"),
    ("Project", PROJECT_NAME, "HAS_GOAL", "Goal", "보안 완결성"),
    ("Project", PROJECT_NAME, "HAS_GOAL", "Goal", "일정 준수"),
    ("Project", PROJECT_NAME, "REPLACES", "Equipment", "백본스위치"),
    ("Project", PROJECT_NAME, "REPLACES", "Equipment", "L4스위치"),
    ("Project", PROJECT_NAME, "COVERS", "Scope", "9개 대상 부대"),
    ("Goal", "무중단 운용 보장", "ACHIEVED_BY", "Strategy", "무중단 순차 교체"),
    ("Goal", "무중단 운용 보장", "ACHIEVED_BY", "Strategy", "현황 실사 및 사전 협의"),
    ("Goal", "완전 호환 및 연동", "ACHIEVED_BY", "Strategy", "설정 이관 및 연동"),
    ("Goal", "완전 호환 및 연동", "VERIFIED_BY", "Strategy", "부대별 인수시험"),
    ("Goal", "보안 완결성", "ACHIEVED_BY", "Strategy", "취약점 전수조치"),
    ("Goal", "보안 완결성", "REQUIRES", "Requirement", "보안기능확인서"),
    ("Goal", "일정 준수", "ACHIEVED_BY", "Strategy", "권역별 전담조직"),
    ("Goal", "일정 준수", "ACHIEVED_BY", "Strategy", "일정 모니터링 및 예비자원 투입"),
    ("Strategy", "무중단 순차 교체", "APPLIES_TO", "Equipment", "백본스위치"),
    ("Strategy", "무중단 순차 교체", "APPLIES_TO", "Equipment", "L4스위치"),
    ("Equipment", "백본스위치", "SUPPORTED_BY", "Requirement", "10년 부품·기술지원"),
    ("Equipment", "L4스위치", "SUPPORTED_BY", "Requirement", "10년 부품·기술지원"),
    ("Strategy", "권역별 전담조직", "SERVES", "Scope", "9개 대상 부대"),
    ("Project", PROJECT_NAME, "REQUIRES", "Requirement", "ISO 45001 기반 안전관리"),
    ("Goal", "무중단 운용 보장", "LEADS_TO", "Outcome", "KNCCS 운용 안정성 향상"),
    ("Goal", "완전 호환 및 연동", "LEADS_TO", "Outcome", "고가용 네트워크 환경"),
    ("Goal", "보안 완결성", "LEADS_TO", "Outcome", "KNCCS 운용 안정성 향상"),
    ("Requirement", "10년 부품·기술지원", "ENABLES", "Outcome", "장기 운용 보장"),
    ("Outcome", "KNCCS 운용 안정성 향상", "ENABLES", "Outcome", "해군 작전지휘통제 능력 강화"),
]


def main():
    brain = Langent(neo4j=True, llm_mode="fake", verbose=False)
    if brain.graph is None:
        raise RuntimeError("Neo4j connection failed in fresh Langent runtime")
    graph = brain.graph

    graph.run_cypher(
        "CREATE CONSTRAINT document_source_unique IF NOT EXISTS "
        "FOR (d:Document) REQUIRE d.source IS UNIQUE"
    )
    graph.run_cypher(
        "CREATE CONSTRAINT chunk_id_unique IF NOT EXISTS "
        "FOR (c:Chunk) REQUIRE c.id IS UNIQUE"
    )

    graph.run_cypher(
        "MERGE (d:Document {source: $source}) "
        "SET d.name=$source, d.format='Markdown', d.derived_from='PDF', "
        "d.project=$project",
        {"source": DOCUMENT_NAME, "project": PROJECT_NAME},
    )

    for label, name, description, _aliases in ENTITIES:
        graph.merge_entity(
            label,
            "name",
            {
                "name": name,
                "description": description,
                "source": DOCUMENT_NAME,
                "project": PROJECT_NAME,
            },
        )
        graph.run_cypher(
            f"MATCH (d:Document {{source:$source}}), (n:{label} {{name:$name}}) "
            "MERGE (d)-[:DESCRIBES]->(n)",
            {"source": DOCUMENT_NAME, "name": name},
        )

    for from_label, from_name, rel, to_label, to_name in RELATIONS:
        graph.create_relation(
            from_label,
            "name",
            from_name,
            rel,
            to_label,
            "name",
            to_name,
            {"source": DOCUMENT_NAME},
        )

    vector_data = brain.vector.get_all_embeddings(limit=10000)
    chunk_rows = []
    mention_rows = []
    for chunk_id, metadata, text in zip(
        vector_data["ids"],
        vector_data["metadatas"],
        vector_data["documents"],
    ):
        if metadata.get("source") != DOCUMENT_NAME and metadata.get("filename") != DOCUMENT_NAME:
            continue
        chunk_rows.append(
            {
                "id": chunk_id,
                "source": DOCUMENT_NAME,
                "chunk_index": metadata.get("chunk_index"),
                "preview": (text or "")[:500],
            }
        )
        compact = (text or "").replace(" ", "").lower()
        for label, name, _description, aliases in ENTITIES:
            if any(alias.replace(" ", "").lower() in compact for alias in aliases):
                mention_rows.append(
                    {"chunk_id": chunk_id, "label": label, "name": name}
                )

    graph.run_cypher(
        "UNWIND $rows AS row "
        "MERGE (c:Chunk {id:row.id}) "
        "SET c.source=row.source, c.chunk_index=row.chunk_index, c.preview=row.preview "
        "WITH c "
        "MATCH (d:Document {source:$source}) "
        "MERGE (d)-[:HAS_CHUNK]->(c)",
        {"rows": chunk_rows, "source": DOCUMENT_NAME},
    )

    for label in sorted({row["label"] for row in mention_rows}):
        rows = [row for row in mention_rows if row["label"] == label]
        graph.run_cypher(
            f"UNWIND $rows AS row "
            f"MATCH (c:Chunk {{id:row.chunk_id}}), (n:{label} {{name:row.name}}) "
            "MERGE (c)-[:MENTIONS]->(n)",
            {"rows": rows},
        )

    schema = graph.get_schema()
    counts = graph.run_cypher(
        "MATCH (d:Document {source:$source}) "
        "OPTIONAL MATCH (d)-[:HAS_CHUNK]->(c:Chunk) "
        "WITH d, count(DISTINCT c) AS chunks "
        "OPTIONAL MATCH (d)-[:DESCRIBES]->(e) "
        "WITH d, chunks, count(DISTINCT e) AS entities "
        "OPTIONAL MATCH (c2:Chunk {source:$source})-[m:MENTIONS]->() "
        "RETURN chunks, entities, count(m) AS mentions",
        {"source": DOCUMENT_NAME},
    )[0]
    relation_count = graph.run_cypher(
        "MATCH ()-[r]->() WHERE r.source=$source RETURN count(r) AS count",
        {"source": DOCUMENT_NAME},
    )[0]["count"]

    report = {
        "document": DOCUMENT_NAME,
        "project": PROJECT_NAME,
        "vector_count": brain.vector.count(),
        "document_chunks_linked": counts["chunks"],
        "semantic_entities": counts["entities"],
        "chunk_entity_mentions": counts["mentions"],
        "semantic_relations": relation_count,
        "graph_schema": schema,
        "neo4j_connected": True,
    }
    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    brain.close()


if __name__ == "__main__":
    main()
