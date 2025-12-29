FROM python:3.13-slim-bookworm as builder
COPY --from=ghcr.io/astral-sh/uv:0.9.18 /uv /bin/uv

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app/backend

# 依存関係ファイルを先にコピー（レイヤーキャッシュの最適化）
COPY pyproject.toml uv.lock ./

# psycopg2 ビルドに必要なパッケージをインストールし、依存関係をインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && uv pip install --system . \
    && apt-get purge -y build-essential libpq-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# 残りのコードをコピー（コード変更時はこのレイヤーのみ再ビルド）
COPY . /app/backend

FROM python:3.13-slim-bookworm
WORKDIR /app/backend
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# psycopg2 実行に必要なランタイムライブラリをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && apt-get purge -y build-essential libpq-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# 依存だけを builder からコピー（同じ python:3.13-slim 系で揃えることが重要）
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/backend .
