from ninja import NinjaAPI, Schema
from opensearchpy import OpenSearch
import os


api = NinjaAPI()


class SearchRequest(Schema):
    search_word: str


@api.post("/search")
def search(request, data: SearchRequest):
    host = "opensearch"
    port = 9200
    auth = (
        os.environ.get("OPENSEARCH_INITIAL_ADMIN_USERNAME"),
        os.environ.get("OPENSEARCH_INITIAL_ADMIN_PASSWORD"),
    )

    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,
    )

    index_name = "classmates"

    query = {
        "size": 5,
        "query": {
            "multi_match": {"query": data.search_word, "fields": ["Name^2", "Sex"]}
        },
    }

    response = client.search(body=query, index=index_name)

    # 検索結果を適切にフォーマット
    hits = response.get("hits", {}).get("hits", [])
    results = [hit["_source"] for hit in hits]

    # totalの取得（OpenSearchのバージョンによって形式が異なる可能性があるため）
    total_obj = response.get("hits", {}).get("total", {})
    if isinstance(total_obj, dict):
        total = total_obj.get("value", 0)
    else:
        total = total_obj or 0

    return {"took": response.get("took", 0), "total": total, "results": results}
