def add_task(tasks):
    n = int(input("How many tasks do you want to add? "))
    for _ in range(n):
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

def show_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def mark_task_done(tasks):
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    actions = {
        "1": add_task,
        "2": show_tasks,
        "3": mark_task_done
    }

    while True:
        print("\n~To-Do List~")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4":
            print("Exiting the To-Do List.")
            break

        # If valid choice, call the function
        if choice in actions:
            actions[choice](tasks)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
