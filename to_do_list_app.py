import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip().split("|") for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task[0]}|{task[1]}\n")

def view_tasks(tasks):
    print("\n--- YOUR TASKS ---")
    for i, (status, task) in enumerate(tasks, 1):
        print(f"{i}. [{'X' if status == 'done' else ' '}] {task}")
    print("------------------")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(("pending", task))
    print(f'Task added: "{task}"')

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num][0] = "done"
            print(f'Task "{tasks[num][1]}" marked as done! ✅')
    except ValueError:
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            deleted = tasks.pop(num)
            print(f'Task "{deleted[1]}" deleted! 🗑️')
    except ValueError:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()