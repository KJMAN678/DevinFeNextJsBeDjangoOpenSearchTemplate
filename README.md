### 検索
```sh
- ダミーデータで検索インデックスを作成
$ docker compose -f docker-compose.mac.yaml exec backend uv run python app/manage.py add_dummy_seach_index
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run python app/manage.py add_dummy_seach_index

- 検索結果を表示
$ docker compose -f docker-compose.mac.yaml exec backend uv run python app/manage.py show_search_result "Alice"
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run python app/manage.py show_search_result "Alice"
```

### Devin

- [Devin's Machine](https://app.devin.ai/workspace) でリポジトリ追加

#### 1.Git Pull
- そのまま

#### 2.Configure Secrets
```sh
# 環境変数用のファイル作成
$ touch .envrc
$ cp .envrc.example .envrc
$ direnv allow
```

- ローカル用
```sh
$ brew install direnv
```
#### 4.Maintain Dependencies
```sh
# ローカルM1Mac用
$ docker compose -f docker-compose.mac.yaml up -d
# Devin用
$ docker compose -f docker-compose.ubuntu.yaml up -d

# コンテナ作り直し
$ ./remake-container.sh mac
$ ./remake-container.sh ubuntu
```

#### 5.SetUp Lint
```sh
# ローカルM1Mac用
$ docker compose -f docker-compose.mac.yaml exec backend uv run ruff check .
$ docker compose -f docker-compose.mac.yaml exec frontend npx next lint

# Devin用
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run ruff check .
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npx next lint
```

- 参考
```sh
$ docker compose -f docker-compose.mac.yaml exec backend uv run ruff format 
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run ruff format 

$ docker compose -f docker-compose.mac.yaml exec backend uv run ruff check --fix .
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run ruff check --fix .
```

#### 6.SetUp Tests
- no tests ran in 0.00s だと Devin の Verify が通らないっぽい
```sh
# ローカルM1Mac用
$ docker compose -f docker-compose.mac.yaml exec backend uv run pytest
$ docker compose -f docker-compose.mac.yaml exec frontend npm run test

# Devin用
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run pytest
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npm run test

# Playwright
# ローカルM1Mac用
$ docker compose -f docker-compose.mac.yaml exec frontend npx playwright test --project firefox

# Devin用
# Playwright
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npx playwright test --project firefox
```

### 7.Setup Local App

```sh
$ http://localhost:3000/ がフロントエンドのURL
$ http://localhost:8000/ がバックエンドのURL
$ http://localhost:5601/ が OpenSearch-Dashboards のURL
```

#### 8.Additional Notes
- 必ず日本語で回答してください
を入力

### Django
- app 追加
```sh
# ローカルM1Mac用
$ mkdir -p backend/app/search
$ docker compose -f docker-compose.mac.yaml exec backend uv run django-admin startapp search app/search
$ docker compose -f docker-compose.mac.yaml exec backend uv run python app/manage.py makemigrations
$ docker compose -f docker-compose.mac.yaml exec backend uv run python app/manage.py migrate

# Devin用
$ mkdir -p backend/app/search
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run django-admin startapp search app/search
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run python app/manage.py makemigrations
$ docker compose -f docker-compose.ubuntu.yaml exec backend uv run python app/manage.py migrate
```


### フロントエンドのバージョンアップ

```sh
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npx npm-check-updates -u
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npx npm-check-updates -u --target minor
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npx npm-check-updates -u --target patch
$ docker compose -f docker-compose.ubuntu.yaml exec frontend npm install
```
