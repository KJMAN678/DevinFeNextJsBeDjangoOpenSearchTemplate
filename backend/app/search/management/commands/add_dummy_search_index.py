from django.core.management.base import BaseCommand
from faker import Faker

from search.constants import opensearch_client


class Command(BaseCommand):
    help = "add dummy search index"

    def handle(self, *args, **options):
        client = opensearch_client()

        index_name = "classmates"
        if client.indices.exists(index=index_name):
            client.indices.delete(index=index_name)

        fake = Faker("ja_JP")
        for _ in range(100):
            data = {
                "Name": fake.name(),
                "Age": fake.random_int(min=18, max=100),
                "Sex": fake.random_element(elements=("f", "m")),
            }
            client.index(index=index_name, body=data, refresh=True)

        self.stdout.write("Added 100 dummy search index")
