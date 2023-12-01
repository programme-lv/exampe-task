#!/usr/bin/env python3
import csv
import random
import pathlib
import random
import subprocess
import os
random.seed(123)
DIR = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
ROOT = DIR.parent

param_path = ROOT.joinpath("generation").joinpath("params.csv")
params = []
with open(DIR.joinpath("params.csv"),"r") as f:
    params = list(csv.reader(f,delimiter="\t"))

sol_src_path = ROOT.joinpath("solutions").joinpath("jonathan-uy.cpp")
gen_src_path = ROOT.joinpath("generation").joinpath("generator.cpp")
temp_dir = ROOT.joinpath("temporary")
if not temp_dir.exists():
    temp_dir.mkdir()
sol_exe_path = temp_dir.joinpath("solution")
gen_exe_path = temp_dir.joinpath("generator")

print("Compiling...")
subprocess.run(["g++", "-std=c++17", "-O2", "-o", str(sol_exe_path), str(sol_src_path)])
subprocess.run(["g++", "-std=c++17", "-O2", "-o", str(gen_exe_path), str(gen_src_path)])

test_dir = ROOT.joinpath("tests")
if not test_dir.exists():
    test_dir.mkdir()

for row in params[1:]:
    test, N, M = row
    test_in_path = test_dir.joinpath(f"{test}.in")
    test_ans_path = test_dir.joinpath(f"{test}.ans")

    print(f"Running generator for test {test}...")
    with open(test_in_path, "w") as f:
        subprocess.run([str(gen_exe_path), str(N), str(M)], stdout=f)

    print(f"Running solution for test {test}...")
    with open(test_in_path, "r") as f:
        with open(test_ans_path, "w") as g:
            subprocess.run([str(sol_exe_path)], stdin=f, stdout=g)

