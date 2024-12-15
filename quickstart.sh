#!/bin/bash

cd "$(dirname "$0")"
mkdir downloads
export DOWNLOAD_PATH=./downloads
docker compose up -d --build