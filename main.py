import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "status": "todo"})
    save_tasks(tasks)
    print(f"✅ Task added successfully (ID: {len(tasks)})")

def update_task(task_id, description):
    tasks = load_tasks()
    index = task_id - 1
    if 0 <= index < len(tasks):
        tasks[index]['description'] = description
        save_tasks(tasks)
        print(f"✏️ Task {task_id} updated successfully.")
    else:
        print("⚠️ Invalid task ID.")

def delete_task(task_id):
    tasks = load_tasks()
    index = task_id - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task {task_id} deleted successfully.")
    else:
        print("⚠️ Invalid task ID.")

def mark_task(task_id, status):
    tasks = load_tasks()
    index = task_id - 1
    if 0 <= index < len(tasks):
        tasks[index]['status'] = status
        save_tasks(tasks)
        print(f"✅ Task {task_id} marked as {status}.")
    else:
        print("⚠️ Invalid task ID.")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        status = task.get('status', 'unknown')
        description = task.get('description', 'No description')
        status_icon = {
            'todo': '📝',
            'in-progress': '⏳',
            'done': '✅'
        }.get(status, '')
        if filter_status is None or status == filter_status:
            print(f"[{idx}] {status_icon} {description} ({status})")

def clean_tasks():
    tasks = load_tasks()
    cleaned_tasks = [
        task for task in tasks
        if 'description' in task and 'status' in task
    ]
    save_tasks(cleaned_tasks)
    print(f"🧹 Cleaned tasks file. Removed {len(tasks) - len(cleaned_tasks)} invalid tasks.")

def main():
    if len(sys.argv) < 2:
        print("⚠️ No command provided.")
        return

    command = sys.argv[1]
    
    if command == 'add' and len(sys.argv) >= 3:
        add_task(sys.argv[2])
    elif command == 'update' and len(sys.argv) >= 4:
        try:
            task_id = int(sys.argv[2])
            update_task(task_id, sys.argv[3])
        except ValueError:
            print("⚠️ Task ID must be a number.")
    elif command == 'delete' and len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("⚠️ Task ID must be a number.")
    elif command == 'mark-in-progress' and len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, 'in-progress')
        except ValueError:
            print("⚠️ Task ID must be a number.")
    elif command == 'mark-done' and len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, 'done')
        except ValueError:
            print("⚠️ Task ID must be a number.")
    elif command == 'list':
        if len(sys.argv) == 3:
            status_map = {'done': 'done', 'todo': 'todo', 'in-progress': 'in-progress'}
            filter_status = status_map.get(sys.argv[2].lower())
            if filter_status:
                list_tasks(filter_status)
            else:
                print("⚠️ Unknown status filter. Use: done, todo, in-progress")
        else:
            list_tasks()
    elif command == 'clean':
        clean_tasks()
    else:
        print("⚠️ Unknown command.")

if __name__ == '__main__':
    main()
