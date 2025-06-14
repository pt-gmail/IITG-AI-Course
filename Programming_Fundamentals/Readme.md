## Setup Done before running application
<p>pip install jq - For parsing json files</p>
<p>pip install bcrypt - For encoding and decoding password</p>
<p>pip install uuid - For creating a new task id for each task</p>

## Json Files Created to store user credentials and tasks
Credentials.json file will look something like this (It will be used to store username and hashed password)<br>
<pre>{
    "user_credentials": [
    ]
}
</pre>
<br>
Tasks.json file will look something like this (It will be used to store tasks of all users)<br>
<pre>
{}
</pre>

## Running Python File 
<pre>
>> python3 .\Task_Manager_User_Authentication.py
==================================================
Welcome to Task Manager Authentication Application    
==================================================    

==================================================    
Options are as follows: 
Enter 1 - Create new account
Enter 2 - Login (if you have already existing account)
Enter 3 - Exit application
Enter option:
</pre>

## User Registration
On running python file we get options to create acconunt / login /exit <br>
On entering 1, lets create an account with username - test, password - test_pwd <br>
<pre>
Enter option: 1

==================================================
Creating a new account
==================================================
Enter username to create new account: test
Enter password to create new account: test_pwd
Username: test, created and added to database
</pre>
Lets see how credentials.json looks now
<pre>
{
    "user_credentials": [
        {
            "username": "test",
            "password": "$2b$12$yTkP0OibW21YQlRDXrhaH.zmshQ4C9uPwOK35BrNihtTjqdGRhtz."
        }
    ]
}
</pre>
Lets see what happens if we create account again with same username - It will throw an error
<pre>
Enter option: 1

==================================================
Creating a new account
==================================================
Enter username to create new account: test
Enter password to create new account: 1234
This username already exists in the database!! Please try another username
</pre>

## User Login
If we login using a username which does not exit we get No such user exists message 
<pre>
Enter option: 2

==================================================
Let us login to Task Manager User Authentication
==================================================
Enter username to login: abc
Enter password to login: abc
No such user exists
</pre>
If we login using incorrect password 
<pre>
Enter option: 2

==================================================
Let us login to Task Manager User Authentication
==================================================
Enter username to login: test
Enter password to login: 12 
Incorrect password
</pre>
If we login using correct username and correct password we will get task manager menu
<pre>
==================================================
Let us login to Task Manager User Authentication
==================================================
Enter username to login: test
Enter password to login: test_pwd
Login Successful
==================================================
Tasks options are as follows:
Enter ViewAll - To view all your tasks
Enter Create - To create a new task
Enter Update - To mark a task as completed
Enter Delete - To delete a task
Enter Exit - To logout

Enter Task Manager Option:
</pre>

## Task Manager 
Lets give ViewAll as input 
<pre>
Enter Task Manager Option: ViewAll
=======================================================================================================================
Viewing All your tasks -

You have not added any tasks yet
=======================================================================================================================
</pre>
Creating new tasks 
<pre>
Enter Task Manager Option: Create
==================================================
Creating a new task -

Please enter task description: new task 1 - read books
New Task added to your list
==================================================
</pre>
Lets see tasks.json now, a new key with username is created and tasks array corresponding to it is created. Initial status of task is pending. And a unique id is added to task.
<pre>
{
    "test": [
        {
            "task_id": "3d410051-e134-4a3b-8b0f-ba55d97e6bde",
            "task_description": "new task 1 - read books",
            "status": "pending"
        }
    ]
}
</pre>
Lets add few more tasks and see how tasks.json looks 
<pre>
{
    "test": [
        {
            "task_id": "3d410051-e134-4a3b-8b0f-ba55d97e6bde",
            "task_description": "new task 1 - read books",
            "status": "pending"
        },
        {
            "task_id": "78637674-f22e-4e8a-a6e4-5887386d35c3",
            "task_description": "Task - Drive Car",
            "status": "pending"
        },
        {
            "task_id": "b495b734-0dd9-4b75-a37c-c7f9aaeda844",
            "task_description": "Task - get veggies",
            "status": "pending"
        }
    ]
}
</pre>
Now lets do ViewAll option
<pre>
Enter Task Manager Option: ViewAll
=======================================================================================================================
Viewing All your tasks -

ID -  3d410051-e134-4a3b-8b0f-ba55d97e6bde , Desc -  new task 1 - read books , Status -  pending
ID -  78637674-f22e-4e8a-a6e4-5887386d35c3 , Desc -  Task - Drive Car , Status -  pending
ID -  b495b734-0dd9-4b75-a37c-c7f9aaeda844 , Desc -  Task - get veggies , Status -  pending
=======================================================================================================================
</pre>
Lets mark a task completed using Update option, status will change to completed
<pre>
Enter Task Manager Option: Update
==================================================
Enter task id which you have to mark as complete: b495b734-0dd9-4b75-a37c-c7f9aaeda844
Task successfully marked as complete
==================================================
==================================================
Tasks options are as follows:
Enter ViewAll - To view all your tasks
Enter Create - To create a new task
Enter Update - To mark a task as completed        
Enter Delete - To delete a task
Enter Exit - To logout

Enter Task Manager Option: ViewAll
=======================================================================================================================
Viewing All your tasks -

ID -  3d410051-e134-4a3b-8b0f-ba55d97e6bde , Desc -  new task 1 - read books , Status -  pending
ID -  78637674-f22e-4e8a-a6e4-5887386d35c3 , Desc -  Task - Drive Car , Status -  pending
ID -  b495b734-0dd9-4b75-a37c-c7f9aaeda844 , Desc -  Task - get veggies , Status -  Completed
=======================================================================================================================
</pre>
Deleting a task 
<pre>
Enter Task Manager Option: Delete
==================================================
Enter task id which you have to delete: 78637674-f22e-4e8a-a6e4-5887386d35c3
Task successfully deleted
==================================================
==================================================
Tasks options are as follows:
Enter ViewAll - To view all your tasks
Enter Create - To create a new task
Enter Update - To mark a task as completed
Enter Delete - To delete a task
Enter Exit - To logout

Enter Task Manager Option: ViewAll
=======================================================================================================================
Viewing All your tasks -

ID -  3d410051-e134-4a3b-8b0f-ba55d97e6bde , Desc -  new task 1 - read books , Status -  pending
ID -  b495b734-0dd9-4b75-a37c-c7f9aaeda844 , Desc -  Task - get veggies , Status -  Completed
=======================================================================================================================
</pre>

## Lets create more users and tasks and look how credentails.json and tasks.json looks like
Credentials.json
<pre>
{
    "user_credentials": [
        {
            "username": "test",
            "password": "$2b$12$yTkP0OibW21YQlRDXrhaH.zmshQ4C9uPwOK35BrNihtTjqdGRhtz."
        },
        {
            "username": "Prerna",
            "password": "$2b$12$c5N5xUGsF8Xs8wcB9zJG1uXN7..tkBkFDu5.LCplFcXKYbx32bSni"
        }
    ]
}
</pre>
Tasks.json
<pre>
{
    "test": [
        {
            "task_id": "3d410051-e134-4a3b-8b0f-ba55d97e6bde",
            "task_description": "new task 1 - read books",
            "status": "pending"
        },
        {
            "task_id": "b495b734-0dd9-4b75-a37c-c7f9aaeda844",
            "task_description": "Task - get veggies",
            "status": "Completed"
        }
    ],
    "Prerna": [
        {
            "task_id": "8c71fb24-9e14-4aca-bf56-5ae54cf01492",
            "task_description": "writing notes",
            "status": "Completed"
        }
    ]
}
</pre>
