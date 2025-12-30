import os

from django.core.management.base import BaseCommand
from opensearchpy import OpenSearch

from search.constants import opensearch_client


class Command(BaseCommand):
    help = "Run a search on the 'classmates' index and print the raw response"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("search_word", nargs=1, type=str)

    def handle(self, *args, **options):
        client = opensearch_client()

        index_name = "classmates"
        q = options["search_word"][0]
        query = {
            "size": 5,
            "query": {"multi_match": {"query": q, "fields": ["Name^2", "Sex"]}},
        }

        response = client.search(body=query, index=index_name)
        self.stdout.write(f"{response}", ending="")
