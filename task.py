"""
Task Tracker CLI - Simple command-line to-do manager
Author: Siqi
Description:
This script allows users to add, list, update, mark, and delete tasks.
Tasks are stored in a JSON file in the current directory.
"""

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

#Load and save tasks

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
        return []

    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON format. The file has been reset to an empty task list.")
            return []

def save_tasks(tasks):
    with open(TASKS_FILE,'w') as f:
        json.dump(tasks, f, indent=2)


#Add a task

def add_task(description):
   tasks = load_tasks()
   new_id = max([task['id'] for task in tasks], default=0) + 1
   created_at = datetime.now().isoformat()
   update_at = created_at
   task = {
      "id": new_id,
      "description": description,
      "status": "todo",
      "createdAt": created_at,
      "updatedAt": update_at
   }
   tasks.append(task)
   save_tasks(tasks)
   print(f"✅ Task added successfully (ID: {new_id})")


#Delete a task

def delete_task(task_id = None, description=None):

    tasks = load_tasks()

    if task_id is not None:    
        updated_tasks = [task for task in tasks if task["id"] != task_id]
        if len(updated_tasks) == tasks:
            print(f"⚠️ Task {task_id} not found.")
        else:
            save_tasks(updated_tasks)
            print(f"🗑️ Task {task_id} deleted.")
        return
    
    if description is not None:
        matches = [task for task in tasks if task["description"] == description]
        if len(matches) == 0:
            print(f"⚠️ Task {description} not found.")
            return
        elif len(matches) == 1:
            tasks.remove(matches[0])
            save_tasks(tasks)
            print(f"🗑️ Task {description} deleted.")
            return
        else:
            print(f"⚠️ Found multiple tasks with description '{description}'. Please specify the task ID.")
            for task in matches:
                print(f"ID: {task['id']} | Status: {task['status']} | Created: {task['createdAt']} | Updated: {task['updatedAt']}")
            return
    
    print("⚠️ Please provide either a task_id or a description to delete.")


#Update a task

def update_task(task_id = None, new_description = None):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"✍️ Task {task_id} updated successfully.")
            return
        else:
            print(f"⚠️ Task {task_id} not found.")


#Mark a state

def mark_task_status(task_id, new_status):
    valid_statuses = ["todo", "in-progress", "done"]
    if new_status not in valid_statuses:
        print(f"⚠️ Invalid status: '{new_status}'. Must be one of {valid_statuses}.")
        return
    
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"🔖 Task {task_id} marked as '{new_status}'.")
            return
    
    print(f"⚠️ Task {task_id} not found.")


#List tasks

def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        valid_statuses = ["todo", "in-progress", "done"]
        if status not in valid_statuses:
            print(f"⚠️ Invalid status: '{status}'. Use one of {valid_statuses}.")
            return
        tasks = [task for task in tasks if task["status"] == status]
        print(f"📋 Tasks with status '{status}':\n")
    else:
        print("📋 All Tasks:\n")

    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        print(f"- ID: {task['id']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {task['status']}")
        print(f"  Created: {task['createdAt']}")
        print(f"  Updated: {task['updatedAt']}")
        print("-" * 30)


     # ---- 所有函数定义结束后 ----

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="📝 Task Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks or tasks with one status")
    list_parser.add_argument("--status", choices=["todo", "in-progress", "done"], help="Filter by status")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task with ID or description")
    delete_parser.add_argument("--id", type=int, help="Task ID")
    delete_parser.add_argument("--description", help="Task description")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task description")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="New description")

    # Mark command
    mark_parser = subparsers.add_parser("mark", help="Mark task status")
    mark_parser.add_argument("id", type=int, help="Task ID")
    mark_parser.add_argument("status", choices=["todo", "in-progress", "done"], help="New status")

    args = parser.parse_args()

    # Dispatcher logic
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "delete":
        delete_task(task_id=args.id, description=args.description)
    elif args.command == "update":
        update_task(task_id=args.id, new_description=args.description)
    elif args.command == "mark":
        mark_task_status(task_id=args.id, new_status=args.status)
    else:
        parser.print_help()
