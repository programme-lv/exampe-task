# Programme.lv example task structure

During runtime of [programme.lv](https://programme.lv/) tasks are kept in the database
however they can be both imported and exported
and this is an example of a task in such state.

The necessity of the exported FS format can be justified by the following reasons:
- the task author might want to edit the task offline;
- the task author is used to preparing tasks on other platform;
- ease of backup and integration into other platforms.

## Notes

`temporary` directory can contain compiled executables and other files except tests
that can be derived from the original state and can be safely deleted.

`environment` directory contains all the files that should be adjacent to the executable during execution.
