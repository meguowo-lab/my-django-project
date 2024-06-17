#!/usr/bin/env bash

python -m grpc_tools.protoc -I./newsapp/proto --python_out=./newsapp/proto --pyi_out=./newsapp/proto --grpc_python_out=./newsapp/proto  ./newsapp/proto/api.proto

echo ""

read w