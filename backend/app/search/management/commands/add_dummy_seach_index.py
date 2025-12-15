import os

from opensearchpy import OpenSearch

from django.core.management.base import BaseCommand
from faker import Faker

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
            ssl_show_warn=False,
        )

        index_name = "classmates"
        if client.indices.exists(index=index_name):
            client.indices.delete(index=index_name)
            
        fake = Faker()
        for _ in range(100):
            data = {
                "Name": fake.name(),
                "Age": fake.random_int(min=18, max=100),
                "Sex": fake.random_element(elements=("f", "m")),
            }
            client.index(index=index_name, body=data, refresh=True)

        self.stdout.write(f"Added 100 dummy search index")
