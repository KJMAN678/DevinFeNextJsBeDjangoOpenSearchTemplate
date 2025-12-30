import os
from functools import lru_cache

from config import settings
from opensearchpy import OpenSearch


@lru_cache(maxsize=1)
def opensearch_client():
    host = "opensearch"
    port = 9200
    auth = (
        os.environ.get("OPENSEARCH_INITIAL_ADMIN_USERNAME"),
        os.environ.get("OPENSEARCH_INITIAL_ADMIN_PASSWORD"),
    )

    if settings.DEBUG:
        verify_serts = False
    else:
        verify_serts = True

    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=verify_serts,
    )

    return client
