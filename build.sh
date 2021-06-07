#!/usr/bin/env bash

set -e

rm -rf build
rm -rf dist
rm -rf src/main/proto/im_protobuf.egg-info
pyroma .
protoc -I=src/main/proto --python_out=src/main/proto \
  src/main/proto/informaticsmatters/protobuf/datamanager/*.proto
touch src/main/proto/informaticsmatters/__init__.py
touch src/main/proto/informaticsmatters/protobuf/__init__.py
touch src/main/proto/informaticsmatters/protobuf/datamanager/__init__.py
python setup.py bdist_wheel
