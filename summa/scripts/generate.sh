#!/usr/bin/env bash

ROOT_DIR=$(readlink -f "$(dirname "$0")/..")
TEMP_DIR="$ROOT_DIR/tmp"
GEN_DIR="$ROOT_DIR/generation"

g++ $GEN_DIR/generator.cpp -o $TEMP_DIR/generator

GEN_EXE=$(readlink -f "$TEMP_DIR/generator")

echo $GEN_EXE

