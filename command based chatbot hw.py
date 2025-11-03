import json
import os

def load_tasks():
    if os.path.exists("homework_data.json"):
        with open("homework_data.json", "r") as file:
            try:
                return json.load(file)
            except:
                return []
    else:
        return []

def save_tasks(tasks):
    with open("homework_data.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = input("Enter your homework task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    i = 1
    for task in tasks:
        status = "✓ Done" if task["done"] else "❌ Not done"
        print(str(i) + ") " + task["task"] + " - " + status)
        i = i + 1

def mark_done():
    tasks = load_tasks()
    view_tasks()
    num = input("Enter task number to mark as done: ")
    if num.isdigit():
        index = int(num) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("❌ Invalid task number.")
    else:
        print("❌ Please enter a number.")


def chatbot():
    print("📚 Homework_Helper Chatbot")
    print("Type addtask, viewtasks, markdone or exit")

    while True:
        command = input("You: ")

        if command == "addtask":
            add_task()
        elif command == "viewtasks":
            view_tasks()
        elif command == "markdone":
            mark_done()
        elif command == "exit":
            print("👋 Goodbye!")
            break
        else:
            print("❓ Unknown command. Try again.")


chatbot()

