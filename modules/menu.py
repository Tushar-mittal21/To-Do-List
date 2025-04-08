from colorama import Fore
from modules.task_handler import add_task, display_tasks, edit_task, delete_task, mark_completed


def interactive_menu(tasks):
    while True:
        print(Fore.CYAN + "\nWelcome to To-Do List Manager!" + Fore.RESET)
        print(Fore.WHITE + "1. Add Task\n2. View Tasks\n3. Edit Task\n4. Delete Task\n5. Mark Task as Completed\n6. Exit" + Fore.RESET)
        choice = input(Fore.BLUE + "Enter your choice: " + Fore.RESET)

        if choice == '1':
            desc = input(Fore.LIGHTBLUE_EX +
                         "Enter task description: " + Fore.RESET)
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            add_task(tasks, desc, deadline)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_id = int(input(Fore.LIGHTBLUE_EX +
                          "Enter task ID to edit: " + Fore.RESET))
            new_desc = input(Fore.LIGHTBLUE_EX +
                             "Enter new description (leave blank to keep current): " + Fore.RESET)
            new_deadline = input(Fore.LIGHTBLUE_EX +
                                 "Enter new deadline (leave blank to keep current): " + Fore.RESET)
            edit_task(tasks, task_id, new_desc if new_desc else None,
                      new_deadline if new_deadline else None)
        elif choice == '4':
            task_id = int(input(Fore.LIGHTBLUE_EX +
                          "Enter task ID to delete: " + Fore.RESET))
            delete_task(tasks, task_id)
        elif choice == '5':
            task_id = int(input(Fore.LIGHTBLUE_EX +
                          "Enter task ID to mark as completed: " + Fore.RESET))
            mark_completed(tasks, task_id)
        elif choice == '6':
            break
        else:
            print(Fore.RED + "Invalid choice. Try again." + Fore.RESET)
