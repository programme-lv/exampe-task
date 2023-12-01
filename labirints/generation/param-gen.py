#!/usr/bin/env python3
import csv
import random
import pathlib
import random
import os
random.seed(123)
DIR = os.path.dirname(os.path.realpath(__file__))

subtasks = [
    {"name": "1", "N_min": 2, "N_max": 10, "M_min": 2, "M_max": 10, "tests": 10},
    {"name": "2", "N_min": 10, "N_max": 100, "M_min": 10, "M_max": 100, "tests": 10},
    {"name": "3", "N_min": 100, "N_max": 1000, "M_min": 100, "M_max": 1000, "tests": 10},
    {"name": "4", "N_min": 1000, "N_max": 1000, "M_min": 1000, "M_max": 1000, "tests": 2},
]

params = [("test","N", "M")]

for st in subtasks:
    for i in range(st["tests"]):
        test = f"{st['name']}-{str(i+1).zfill(3)}"
        N = random.randint(st["N_min"], st["N_max"])
        M = random.randint(st["M_min"], st["M_max"])
        params.append((test, str(N), str(M)))

with open(pathlib.Path(DIR).joinpath("params.csv"),"w") as f:
    csv.writer(f,delimiter="\t").writerows(params)