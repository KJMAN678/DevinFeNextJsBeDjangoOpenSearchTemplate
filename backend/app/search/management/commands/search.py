import os

from opensearchpy import OpenSearch

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
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
        data = {"Name": "Alice", "Age": 21, "Sex": "f"}

        if client.indices.exists(index=index_name):
            client.indices.delete(index=index_name)
        client.index(index=index_name, body=data, refresh=True)

        q = "Alice"
        query = {
            "size": 5,
            "query": {"multi_match": {"query": q, "fields": ["Name^2", "Sex"]}},
        }

        response = client.search(body=query, index=index_name)
        self.stdout.write(f"{response}", ending="")
