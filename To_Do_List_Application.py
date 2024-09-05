intro = "Welcome to the To-Do List App! Type 'menu' for a list of of options."
menu = "Menu:\n 1. Add a Task\n 2. View Tasks\n 3. Mark a Task as Complete\n 4. Delete a Task\n 5. Quit Application"
to_do_list = []

class TaskNotFound(Exception):
    def __init__(self, message):
        self.message = message

def start_app():
    print(intro)
    print(menu)

def display_menu():
    print(menu)

def add_task():
    new_task = input("What task would you like to add to your To-Do List?: ")
    task_status = "Status: Incomplete"
    task_item = (f"{new_task}: {task_status}")
    to_do_list.append(task_item)
    print(f"{task_item} has been added to your To-Do List.")

def view_tasks():
    print(f"To-Do List: {to_do_list}")

def complete_task():
    check_task_status = (input("What task would you like to mark complete?: "))
    update_task_status = (f"{check_task_status}: Status: Incomplete")
    for task in to_do_list:
        if task == update_task_status:
            to_do_list.remove(task)
            task_status_update = "Status: Complete"
            task_item_update = (f"{check_task_status}: {task_status_update}")
            to_do_list.append(task_item_update)
            print(task_item_update)

def delete_task():
    delete_task = (input("What task would you like to delete?: "))
    incomplete_task = (f"{delete_task}: Status: Incomplete")
    complete_task = (f"{delete_task}: Status: Complete")
    for task in to_do_list:
        if task == complete_task:
            to_do_list.remove(task)
            print(f"{delete_task} has been removed from the To-Do List.")
        elif task == incomplete_task:
            to_do_list.remove(task)
            print(f"{delete_task} has been removed from the To-Do List.")

start_app()
while True:
    prompt = input("What would you like to do?: ").lower()
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
    
    continue_input = input("Would you like to continue using this application? (yes/no): ")
    if continue_input == "no":
        break
    elif continue_input == "yes":
        continue
    else:
        continue_input = input("Error: I did not understand your response. Would you like to continue using this application> (yes/no): ")
