intro = "Welcome to the To-Do List App! Type 'menu' for a list of of options."
prompt = input("What would you like to do?: ").lower()
to_do_list = []

class TaskNotFound(Exception):
    def __init__(self, message):
        self.message = message

def display_menu():
    print("Menu:\n 1. Add a Task\n 2. View Tasks\n 3. Mark a Task as Complete\n 4. Delete a Task\n 5. Quit Application")
    prompt = input("What would you like to do?: ").lower()

def add_task():
    try:
        new_task = input("What task would you like to add to your To-Do List?: ").capitalize
        task_status = "Incomplete"
        if new_task.isalpha():
            task_item = (f"{new_task}: {task_status}")
        else:
            raise ValueError
    except ValueError:
        print("The information you entered is not a task. Please enter a task using words.")
    else:
        to_do_list.append(task_item)

def view_tasks():
    print(f"To-Do List: {to_do_list}")

def complete_task():
    try:
        update_task_status = ((input("What task would you like to mark complete?: ") + ": Incomplete")).capitalize
        for task in to_do_list:
            if update_task_status == task:
                task_status_update = "Complete"
                task_item_update = (f"{update_task_status}: {task_status_update}")
                to_do_list.replace(task, task_item_update)
            else:
                raise TaskNotFound("The task you have entered is not on the To-Do List. Please try again.")
    except TaskNotFound as e:
        print(f"Error: {e.message}")

def delete_task():
    try:
        delete_task = (input("What task would you like to delete?: ")).capitalize
        for task in to_do_list:
            completed_task = f"{task} + Complete"
            incomplete_task = f"{task} + Incomplete"
            if delete_task == completed_task:
                to_do_list.remove(task)
            elif delete_task == incomplete_task:
                to_do_list.remove(task)
            else:
                raise TaskNotFound("The task you have entered is not on the To-Do List. Please try again.")
    except TaskNotFound as e:
        print(f"Error: {e.message}")

def quit_app():
    while True:
        continue_input = input("Would you like to continue using this application? (yes/no): ")
        if continue_input == "yes":
            prompt = input("What would you like to do?: ").lower()
        elif continue_input == "no":
            break
        elif prompt == "quit":
            break
        else:
            prompt = input("I'm sorry, an unknown error occurred. What would you like to do?: ").lower()

if prompt == "menu":
    display_menu()
elif prompt == "add a task":
    add_task()
elif prompt == "view tasks":
    view_tasks()
elif prompt == "mark a task as complete":
    complete_task()
elif prompt == "delete a task":
    delete_task()
elif prompt == "quit application":
    quit_app()