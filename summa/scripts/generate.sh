#!/usr/bin/env bash

ROOT_DIR=$(readlink -f "$(dirname "$0")/..")
TEMP_DIR="$ROOT_DIR/temporary"
GEN_DIR="$ROOT_DIR/generation"

if [ ! -f "$GEN_DIR/generator.cpp" ]; then
    echo "generator.cpp not found"
    exit 1
fi

if [ ! -f "$GEN_DIR/generate.jl" ]; then
    echo "generate.jl not found"
    exit 1
fi

if [ ! -d "$TEMP_DIR" ]; then
    echo "creating temporary directory"
    mkdir -p $TEMP_DIR
fi

echo "compiling generator"
g++ -o $TEMP_DIR/generator $GEN_DIR/generator.cpp

GEN_SCRIPT=$(readlink -f "$GEN_DIR/generate.jl")
GEN_EXE=$(readlink -f "$TEMP_DIR/generator")
TEST_DIR="$ROOT_DIR/tests"

if [ -d "$TEST_DIR" ]; then
    echo "removing old test directory"
    rm -r $TEST_DIR
fi

mkdir -p $TEST_DIR

echo "generating tests"
pushd $TEST_DIR
julia $GEN_SCRIPT
popd
