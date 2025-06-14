import json
import jq
import bcrypt
import uuid

def get_all_user_credentials():
    with open('credentials.json') as c:
        global load_credentials_data
        load_credentials_data = json.load(c)
        username_query = '.user_credentials[].username'
        global all_usernames_list
        all_usernames_list = jq.compile(username_query).input(load_credentials_data).all()

# Registration: Create a function to prompt the user to enter a username and password 
def register_user():
    print("\n==================================================")
    print("Creating a new account")
    print("==================================================")
    username = input("Enter username to create new account: ")
    password = input("Enter password to create new account: ")
    if(username in all_usernames_list):
        print("This username already exists in the database!! Please try another username\n")
    else:
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = {
            "username": username,
            "password": hashed_pw
        }
        load_credentials_data["user_credentials"].append(new_user)
        with open('credentials.json', 'w') as f:
            json.dump(load_credentials_data, f, indent=4)
        print("Username: " + username + ", created and added to database")
        print("")

# Create a function to prompt the user for their username and password
def login_user():
    print("\n==================================================")
    print("Let us login to Task Manager User Authentication")
    print("==================================================")
    username = input("Enter username to login: ")
    password = input("Enter password to login: ")
    if(username in all_usernames_list):
        user_record = next((user for user in load_credentials_data["user_credentials"] if user["username"] == username), None)
        if(bcrypt.checkpw(password.encode('utf-8'), user_record["password"].encode('utf-8'))):
            print("Login Successful")
            global logged_in_user
            logged_in_user = username
            tasks_menu_option()
        else:
            print("Incorrect password\n")
    else:
        print("No such user exists\n")

def tasks_menu_option():
    # Loading tasks file
    with open('tasks.json') as c:
        global tasks_data
        tasks_data = json.load(c)
        if(logged_in_user not in tasks_data):
            tasks_data[logged_in_user] = []
    while(True):
        print("==================================================")
        print("Tasks options are as follows: ")
        print("Enter ViewAll - To view all your tasks")
        print("Enter Create - To create a new task")
        print("Enter Update - To mark a task as completed")
        print("Enter Delete - To delete a task")
        print("Enter Exit - To logout")
        print("")
        option = input("Enter Task Manager Option: ")
        if(option == "ViewAll"):
            view_tasks()
        elif(option == "Create"):
            create_task()
        elif(option == "Delete"):
            delete_task()
        elif(option == "Update"):
            mark_as_completed()
        elif(option == "Exit"): 
            break
        else:
            print("No matching option")

# Create a function to retrieve and display all tasks for the logged-in user
def view_tasks():
    print("=======================================================================================================================")
    print("Viewing All your tasks - \n")
    if(len(tasks_data[logged_in_user]) == 0):
        print("You have not added any tasks yet")
    else:
        for t in tasks_data[logged_in_user]:
            print("ID - ", t["task_id"], ", Desc - ", t["task_description"], ", Status - ", t["status"])
    print("=======================================================================================================================\n")



# Create a function that prompts the user for a task description. Assign a unique task ID and set the status to Pending 
def create_task():
    print("==================================================")
    print("Creating a new task - \n")
    task_description = input("Please enter task description: ")
    task = {
        'task_id': str(uuid.uuid4()),
        'task_description': task_description,
        'status': 'pending'
    }
    tasks_data[logged_in_user].append(task)
    with open('tasks.json', 'w') as f:
        json.dump(tasks_data, f, indent=4)
    print("New Task added to your list")
    print("==================================================")

# Create a function that allows the user to select a task by its ID and delete it from their task list 
def delete_task():
    print("==================================================")
    task_id_to_be_deleted = input("Enter task id which you have to delete: ")
    task_record = next((t for t in tasks_data[logged_in_user] if t["task_id"] == task_id_to_be_deleted), None)
    if(task_record):
        tasks_data[logged_in_user] = [t for t in tasks_data[logged_in_user] if t["task_id"] != task_id_to_be_deleted]
        with open('tasks.json', 'w') as f:
            json.dump(tasks_data, f, indent=4)
        print("Task successfully deleted")
    else:
        print("No such task found")
    print("==================================================")

# Create a function that allows the user to select a task by its ID and update its status to Completed 
def mark_as_completed():
    print("==================================================")
    task_id_to_be_completed = input("Enter task id which you have to mark as complete: ")
    task_record = next((t for t in tasks_data[logged_in_user] if t["task_id"] == task_id_to_be_completed), None)
    if(task_record):
        completed_task_dict = [t for t in tasks_data[logged_in_user] if t["task_id"] == task_id_to_be_completed][0]
        completed_task_dict["status"] = "Completed"
        tasks_data[logged_in_user] = [t for t in tasks_data[logged_in_user] if t["task_id"] != task_id_to_be_completed]
        tasks_data[logged_in_user].append(completed_task_dict)
        with open('tasks.json', 'w') as f:
            json.dump(tasks_data, f, indent=4)
        print("Task successfully marked as complete")
    else:
        print("No such task found")
    print("==================================================")  

print("==================================================")
print("Welcome to Task Manager Authentication Application")
print("==================================================")
print("")
print("==================================================")
while(True):
    print("Options are as follows: ")
    print("Enter 1 - Create new account")
    print("Enter 2 - Login (if you have already existing account)")
    print("Enter 3 - Exit application")
    option = int(input("Enter option: "))
    get_all_user_credentials()
    if(option == 1):
        register_user()
    elif(option == 2):
        login_user()
    elif(option == 3):
        break
    else:
        print("Incorrect option")
