import argparse
from modules.task_handler import add_task, display_tasks, edit_task, delete_task, mark_completed

def handle_cli(tasks):
    parser = argparse.ArgumentParser(description="CLI To-Do List Manager")
    parser.add_argument('--add', help='Add a new task')
    parser.add_argument('--deadline', help='Deadline for the new or edited task')
    parser.add_argument('--view', action='store_true', help='View all tasks')
    parser.add_argument('--edit', type=int, help='Edit task with given ID')
    parser.add_argument('--desc', help='New description for the task')
    parser.add_argument('--delete', type=int, help='Delete task with given ID')
    parser.add_argument('--complete', type=int, help='Mark task as completed by ID')

    args = parser.parse_args()

    if any([args.add, args.view, args.edit, args.delete, args.complete]):
        if args.add and args.deadline:
            add_task(tasks, args.add, args.deadline)
        elif args.view:
            display_tasks(tasks)
        elif args.edit:
            edit_task(tasks, args.edit, args.desc, args.deadline)
        elif args.delete:
            delete_task(tasks, args.delete)
        elif args.complete:
            mark_completed(tasks, args.complete)
        else:
            parser.print_help()
        return True
    return False
