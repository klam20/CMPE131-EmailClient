# Email Client
- Jeffrey Lam (@klam20)
- Bryant Bautista (@bryantbautista)
- Anthony Nguyen (@antiscoder)
- Nicole Nacua (@nnacua)

## Introduction
- This is an email client developed using Python, Flask, and SQLAlchemy
- Users are able to create accounts that enable them to send emails or messages to other recipients

## Technologies used (libraries & versions, helps recruiters)
- SQLAlchemy
- Flask
- Flask-Login
- Flask-wtf
- Wtforms
- Werkzeug.Security

## How to use
- Run run.py using python interpreter
- E.g. python3 run.py

## Functions
- ![image](https://user-images.githubusercontent.com/85579906/235287767-8fadb139-2ea4-417c-afdf-70693011f1ce.png)
- Log-In/Log-Out (Jeffrey)
![image](https://user-images.githubusercontent.com/85579906/235287819-ef52d286-6634-496e-a474-44cb7a1baedc.png)
- Create Account (Nicole)
- ![image](https://user-images.githubusercontent.com/85579906/235287841-0b96ce0d-58a2-4a10-94fa-a79cd1e7ad64.png)
- Delete Account (Jeffrey)
- ![image](https://user-images.githubusercontent.com/85579906/235287850-1c19208b-9c80-49a3-a1bb-00fafa91813e.png)
- Add item to To-Do List (Anthony)
- ![image](https://user-images.githubusercontent.com/85579906/235287873-7630f8a6-3a52-4c03-a48f-6c0b56049c36.png)
- Strikethrough To-Do List item (Anthony)
- Delete Item To-Do List (Anthony)
- ![image](https://user-images.githubusercontent.com/85579906/235287928-cb49f6eb-b888-4d6b-87ad-9e20ab06f542.png)
- Send Email (Nicole)
- ![image](https://user-images.githubusercontent.com/85579906/235287918-6f97807f-d860-45fc-9c5d-ffb6e531125d.png)
- ![image](https://user-images.githubusercontent.com/85579906/235287921-34376fd4-46bb-4c5d-8a90-303f9072a5e3.png)
- Chat Message (Bryant) [WIP]
![image](https://user-images.githubusercontent.com/85579906/235287966-fdd56a55-f1d3-4efa-b7e9-6cc215cfd6f7.png)

## To-Do List
Users can keep track of tasks by adding them to a todo list on the email page. 
Each task is given a discription and a due date which is diplayed on the todo list. 
Users will be able to edit, markoff and delete task

<details><summary><b>Show instructions</b></summary>

### Adding Items
  On the left side of the email page there will be a section dedicated to the todo list
  There are fields for entering a task discription and due date
  After filling out the fields a user can press the "+" button to add that task
  
### Marking Off Items
  Clicking on a task will mark the item off as done
  
### Deleting Items
  There is an "x" button next to each task, clicking on it will delete the corrisonding task
  
### Editing Items
   There is an edit button next to each task, clicking it will put the task into edit mode
   The user can then edit the task discription and due date
   Clicking on the edit button again will submit the changes and take the task out of edit mode
</details>

## Emails
<details><summary><b>Show instructions</b></summary>

### Compose Button
  On the bottom right, there is a compose button where you can create and send emails
  
### Filling out the form
  The minimum details in order to send an email are recipient email address, subject, and content
  
### Adding Attachments
  Additionally, attachments can be added to the email message. Currently supported file formats are []

### Inbox and Viewing
  The inbox has viewing modes for sent and received emails
  Clicking on an email allows you to view its contents

### Deleting Emails
  To delete an email you must first view the contents of the email
  The Delete Email button will delete the email from your view.

</details>


## Chat System

## Account Setup/Details

<details><summary><b>Show instructions</b></summary>

### Registering
  From the home page, you may sign-up for an account by pressing the following button
  You will need to provide an email address and a password
  
### Logging In
  With a created account, you can log-in to access the other features of the web page
  A registered email and password is required.
  
### Logging Out
  You may log-out using this button located at the nav-bar
  
### Deleting Account
   You may delete account using this button located at the nav-bar
   
</details>
