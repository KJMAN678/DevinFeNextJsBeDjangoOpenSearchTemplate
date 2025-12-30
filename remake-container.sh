#!/bin/sh
export ENV="$1"

docker compose -f docker-compose.$ENV.yaml down
docker compose -f docker-compose.$ENV.yaml build --build-arg NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
docker compose -f docker-compose.$ENV.yaml up -d
