#!/bin/sh
uv run python app/manage.py migrate
uv run python app/manage.py createsuperuser --noinput || true
uv run python app/manage.py add_dummy_seach_index || true
uv run python app/manage.py runserver 0.0.0.0:8000
