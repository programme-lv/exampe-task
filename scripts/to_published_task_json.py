#!/usr/bin/env python3

import os
import hashlib
import json
import toml
import sys

def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_file_contents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def process_directory(base_dir):
    data = {}
    sha_to_name = {}
    examples = {}
    statements = {
        "markdown": {
            "lv": {}
        }
    }

    # Load the TOML file
    toml_file_path = os.path.join(base_dir, 'problem.toml')
    data.update(toml.load(toml_file_path))
    
    # Process the examples
    examples_dir = os.path.join(base_dir, 'examples')
    for example_file in os.listdir(examples_dir):
        example_file_path = os.path.join(examples_dir, example_file)
        examples[example_file] = get_file_contents(example_file_path)
    data['examples'] = examples
    
    # Process the tests
    tests_dir = os.path.join(base_dir, 'tests')
    tests = []
    for test_file in os.listdir(tests_dir):
        test_file_path = os.path.join(tests_dir, test_file)
        sha = compute_sha256(test_file_path)
        tests.append(sha)
        sha_to_name[sha] = test_file
    
    data['tests'] = tests
    data['test_sha_to_filename'] = sha_to_name

    # Process the statements
    statements_dir = os.path.join(base_dir, 'statements/md/lv')
    for statement_file in os.listdir(statements_dir):
        statement_file_path = os.path.join(statements_dir, statement_file)
        statements["markdown"]["lv"][statement_file] = get_file_contents(statement_file_path)
    data['statements'] = statements

    # Process the checker
    testlib_checker_file_path = os.path.join(base_dir, 'evaluation', 'checker.cpp')
    if os.path.exists(testlib_checker_file_path):
        data['testlib_checker_cpp'] = get_file_contents(testlib_checker_file_path)

    # Output the data as JSON to stdout
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    process_directory(base_directory)
