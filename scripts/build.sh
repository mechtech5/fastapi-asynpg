#! /usr/bin/env sh

# Exit in case of error
set -e

TAG=${TAG?Variable not set} \
docker-compose \
-f docker-compose.yml \
build

STACK_NAME=${STACK_NAME?Variable not set} \
docker stack rm "${STACK_NAME?Variable not set}"