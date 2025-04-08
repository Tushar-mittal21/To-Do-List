from modules import cli
from modules.menu import interactive_menu
from modules.task_handler import load_tasks

def main():
    tasks = load_tasks()
    if not cli.handle_cli(tasks):
        interactive_menu(tasks)

if __name__ == "__main__":
    main()
