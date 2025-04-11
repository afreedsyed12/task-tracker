# task-tracker

# Adding a new task
main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
main.py update 1 "Buy groceries and cook dinner"
main.py delete 1

# Marking a task as in progress or done
main.py mark-in-progress 1
main.py mark-done 1

# Listing all tasks
main.py list

# Listing tasks by status
main.py list done
main.py list todo
main.py list in-progress
