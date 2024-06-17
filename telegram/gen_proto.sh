#!/usr/bin/env bash

python -m grpc_tools.protoc -I./proto --python_out=./proto --pyi_out=./proto --grpc_python_out=./proto  ./proto/api.proto

echo ""

read w
