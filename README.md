# 📝 Console To-Do List Manager (Python)

A console-based To-Do List manager with both interactive and CLI support using Python.

---

## 🚀 Features

- Add new tasks with deadlines
- View tasks categorized as Pending or Completed
- Edit task descriptions and deadlines
- Delete tasks
- Mark tasks as completed
- Data persists across sessions via `tasks.txt`

---

## 📁 Files Included

| File              | Description                              |
| ----------------- | ---------------------------------------- |
| `main.py`         | Main application script                  |
| `modules`         | Modules of To-Do-List                           |
| `cli.py`          | Handles usage through argparse           |
| `task_handler.py` | Handles all the functionalities of Tasks |
| `menu.py`         | Menu of To-Do-List                       |
| `tasks.txt`       | Stores task data                         |
| `README.md`       | You’re reading it!                       |

---

## ▶️ How to Run

```bash
# 1. Install dependencies (if needed)
pip install colorama

# 2. Run the application
python todo_list.py
```

---

## ▶️ Using argparse

```bash
python main.py --add "Task Name" --deadline 2025-04-15
python main.py --view
```

---

## 🧠 Sample Usage

```bash
Welcome to To-Do List Manager!
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Mark Task as Completed
6. Exit
Enter your choice: 1
```

Made with ❤️ by Tushar Mittal!