# example-task

During runtime of programme.lv tasks are kept in the database
however they can be both imported and exported
and this is an example of a task in such state.

The necessity of the exported FS format can be explained by the following reasons:
- the task author might want to edit the task offline;
- the task author is used to preparing tasks on other platform;
- ease of backup and integration into other platforms.

## File structure

```
.gitignore
examples
|   1.in
|   1.out
|   2.in
|   2.out
generation
|   generator.cpp
|   validator.cpp
solutions
|   kp_100.cpp
|   kp_75.py
statements
|   docx
|   md-lv
|   |   description.md
|   |   input.md
|   |   output.md
|   |   scoring.md
|   pdf
|   |   lv.pdf
temporary
|   generator.out
tests
|   001.ans
|   001.in
|   002.ans
|   002.in
environment
|   data.csv
evaluation
|   checker.cpp
|   interactor.cpp
problem.toml
```

`temporary` directory can contain compiled executables and other files except tests
that can be derived from the original state and can be safely deleted.

`environment` directory contains all the files that should be adjacent to the executable during execution.

## Statement system

The task statement can be either in Markdown format or in PDF format.
We would like to support PDF format, because some might want to see the original statement.

A Markdown statement has the following sections:
- **story** - the story of the task
- **input** - the description of the input format
- **output** - the description of the output format
- **scoring** - the description of the scoring system


## `problem.toml` example

```toml
id = "baobabi"
full_name = "baobabi"
version = "V9"

author = "Krišjānis Petručeņa"
tag_ids = ["brute-force","math","number-theory","ProblemCon++"]

type = "simple"
time_lim_ms = 1000
mem_lim_mb = 256

[[subtasks]]
name = "A=1,B<=10^3"
score = 12
tests = ["002", "010", "011"]
```
