FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.9.10 /uv /bin/uv

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app/backend

# 依存関係ファイルを先にコピー（レイヤーキャッシュの最適化）
COPY pyproject.toml uv.lock ./

# psycopg2 ビルドに必要なパッケージをインストールし、依存関係をインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && uv sync --dev \
    && apt-get purge -y build-essential libpq-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# 残りのコードをコピー（コード変更時はこのレイヤーのみ再ビルド）
COPY . /app/backend
