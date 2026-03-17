# 📘 Assignment: File Handling and Modules

## 🎯 Objective

Practice Python file input/output, error handling, and module organization by building a simple log analyzer program with reusable helper functions.

## 📝 Tasks

### 🛠️ Read and Parse Log File

#### Description
Create a function to read a log file and parse each line into structured records.

#### Requirements
Completed program should:

- Open a text file called `activity.log` in read mode.
- Read all lines and split each line into timestamp, user, and action values.
- Return a list of record dictionaries like `{"timestamp": ..., "user": ..., "action": ...}`.

### 🛠️ Filter and Summarize Data

#### Description
Build a function to filter the parsed records by user and create an action summary.

#### Requirements
Completed program should:

- Accept parsed record list and username as inputs.
- Return only records matching the given username.
- Count actions and print a summary (e.g., `login: 4`, `logout: 3`).

### 🛠️ Organize Module and Handle Missing Files

#### Description
Use a separate module for parsing and reporting logic, and add file-not-found error handling.

#### Requirements
Completed program should:

- Put parsing and filtering functions in `log_utils.py`.
- Import `log_utils` in `main.py` and use it to run analysis.
- Handle `FileNotFoundError` gracefully with a user-friendly message.
