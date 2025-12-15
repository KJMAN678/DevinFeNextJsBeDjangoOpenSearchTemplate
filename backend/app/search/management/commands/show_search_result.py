import os

from opensearchpy import OpenSearch

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("search_word", nargs=1, type=str)

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
        q = options["search_word"][0]
        query = {
            "size": 5,
            "query": {"multi_match": {"query": q, "fields": ["Name^2", "Sex"]}},
        }

        response = client.search(body=query, index=index_name)
        self.stdout.write(f"{response}", ending="")
