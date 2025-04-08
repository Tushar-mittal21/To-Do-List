import os
from datetime import datetime
from colorama import Fore

TASKS_FILE = 'tasks.txt'


def load_tasks():
    tasks = []
    if not os.path.exists(TASKS_FILE):
        open(TASKS_FILE, 'w').close()
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split(',', 3)
            if len(parts) == 4:
                task_id, desc, deadline, status = parts
                tasks.append({
                    'id': int(task_id),
                    'description': desc,
                    'deadline': deadline,
                    'status': status
                })
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(
                f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")


def display_tasks(tasks):
    print(Fore.YELLOW + "\n[Pending]" + Fore.RESET)
    for task in [t for t in tasks if t['status'] == 'Pending']:
        print(
            f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    print(Fore.GREEN + "\n[Completed]" + Fore.RESET)
    for task in [t for t in tasks if t['status'] == 'Completed']:
        print(
            f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")


def add_task(tasks, desc, deadline):
    try:
        datetime.strptime(deadline, '%Y-%m-%d')
        new_id = max([t['id'] for t in tasks], default=0) + 1
        tasks.append({
            'id': new_id,
            'description': desc,
            'deadline': deadline,
            'status': 'Pending'
        })
        save_tasks(tasks)
        print(Fore.GREEN +
              f"Task added successfully! ID: {new_id}" + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Invalid deadline format. Use YYYY-MM-DD." + Fore.RESET)


def edit_task(tasks, task_id, new_desc, new_deadline):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        if new_desc:
            task['description'] = new_desc
        if new_deadline:
            try:
                datetime.strptime(new_deadline, '%Y-%m-%d')
                task['deadline'] = new_deadline
            except ValueError:
                print(Fore.RED + "Invalid date format." + Fore.RESET)
        save_tasks(tasks)
        print(Fore.GREEN + "Task updated." + Fore.RESET)
    else:
        print(Fore.RED + "Task not found." + Fore.RESET)


def delete_task(tasks, task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(Fore.GREEN + "Task deleted." + Fore.RESET)
    else:
        print(Fore.RED + "Task not found." + Fore.RESET)


def mark_completed(tasks, task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        if task['status'] == 'Completed':
            print(Fore.YELLOW + "Task already completed." + Fore.RESET)
        else:
            task['status'] = 'Completed'
            save_tasks(tasks)
            print(Fore.GREEN + "Task marked as completed." + Fore.RESET)
    else:
        print(Fore.RED + "Task not found." + Fore.RESET)
