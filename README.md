# 📝 Task Tracker CLI

A simple and lightweight command-line tool to manage your personal tasks using Python and JSON.

## Features

- Add, update, and delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List all tasks or filter tasks by status
- Data stored locally in `tasks.json`
- Command-line interface (CLI) with helpful descriptions

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task_tracker_CLI.git
   cd task_tracker_CLI
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. No extra dependencies are required — just Python 3!

## Usage

All commands are executed via `task.py`:

### Add a task
```bash
python task.py add "Read a book"
```

### List all tasks
```bash
python task.py list
```

### List tasks by status
```bash
python task.py list --status done
```

### Update a task
```bash
python task.py update --id 1 --description "Read a novel"
```

### Mark a task's status
```bash
python task.py mark --id 1 --status in-progress
```

### Delete a task
```bash
python task.py delete --id 1
```

## Project Structure

```
task_tracker_CLI/
├── task.py           # Main program entry point
├── tasks.json        # Stores all tasks (auto-created)
├── .gitignore        # Ignored files for Git
└── README.md         # Project documentation
```

## ✨ Author

Siqi — 2025  
Built for CLI practice and task management in Python.
