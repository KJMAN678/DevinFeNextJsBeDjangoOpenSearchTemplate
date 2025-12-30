import os

from opensearchpy import OpenSearch


def opensearch_client():
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

    return client
