# Email Client

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Developers](#developers)
- [Installation and Setup](#installation-and-setup)
- [Libraries](#libraries)
- [Functions](#functions)

## Introduction <a name="introduction"></a>

This Email Client is a powerful and user-friendly email application 
developed using Python, Flask, and 
SQLAlchemy. It provides a seamless communication experience, allowing 
users to create accounts and send 
emails or messages to other users. 

With this Email Client, you can stay connected for both personal and 
professional use. For it offers a 
range of features to enhance email communication by ensuring efficiency 
and convenience. 

**Key Features** <a name="key-features"></a> 
- **User-Friendly Interface**: A polished an intuitive interface that 
makes navigating and managing emails 
and messages easy
- **Account Creation**: Simple steps to create an account to access all 
the functionalities and benefits of 
the email client
- **Compose and Send Emails**: Compose and send emails to individuals with 
ease
- **Attachments**: Can attach documents or images to your emails
- **Inbox Management**: Find any email through a search bar or filter 
emails by read/unread
- **Todo List**: Manage your tasks effectively with a built-in todo list 
feature, allowing more 
organization and productivity
- **Chat Feature**: Along with an email system, you can stay connected 
with others through a chat system

**Developers**  <a name="developers"></a>
- Jeffrey Lam (@klam20)
- Bryant Bautista (@bryantbautista)
- Anthony Nguyen (@antiscoder)
- Nicole Nacua (@nnacua)

## Installation and Setup  <a name="installation-and-setup"></a>
1. Clone the repository
2. Navigate to the project directory
3. Install the required dependencies: pip install -r requirements.txt
4. Start the application: python run.py 
5. Open the web browser and visit the link provided in the terminal 
(http://127.0.0.1:5000)

## Libraries <a name=“libraries”></a>
Once you have followed the installation and setup process, you should see 
the list of libraries used in requirements.txt
<details>
<summary> List of Libraries Used </summary>
<ul>
<li>alembic</li>
<li>blinker</li>
<li>click</li>
<li>dnspython</li>
<li>email-validator</li>
<li>Flask</li>
<li>Flask-Login</li>
<li>Flask-Mail</li>
<li>Flask-Migrate</li>
<li>Flask-SQLAlchemy</li>
<li>Flask-Uploads</li>
<li>Flask-WTF</li>
<li>greenlet</li>
<li>idna</li>
<li>itsdangerous</li>
<li>Jinja2</li>
<li>Mako</li>
<li>MarkupSafe</li>
<li>Pillow</li>
<li>SQLAlchemy</li>
<li>typing_extensions</li>
<li>Werkzeug</li>
<li>WTForms</li>
</ul>
</details>

## Functions <a name=“functions”></a>

<details>
<summary>Account Management</summary>
This section covers the various actions related to managing user accounts. 
Here are the instructions for each:

### Registration
- To register for an account, go to the home page and click the “Sign-up” 
button
- Create an email address and password to complete registration
    <details>
    <summary> Show example </summary>
    
    </details>

### Logging In
- Once you have a registered account, use the login feature to access 
other functionalities.
- Enter your registered email and password to log in
    <details>
    <summary> Show example </summary>
    
    </details>

### Logging Out
- To log out, locate the "Log-out" button in the navigation bar and click 
on it
- Logging out will terminate your current session
    <details>
    <summary> Show example </summary>
    
    </details>

### Deleting Account
- If you wish to delete your account, find the "Delete Account" button in 
the navigation bar.
- Click on the button to initiate the account deletion process
    <details>
    <summary> Show example </summary>
    
    </details>
</details>
<details>
<summary> Email Management</summary>
This section provides instructions for managing emails within the 
application. Here are the instructions for each action:

### Compose Button
- Locate the compose button on the bottom right corner
- Click on the compose button to create and send emails
    <details>
    <summary> Show example </summary>
    
    </details>

### Filling out the Form
- To send an email, provide the required information such as the 
recipient's email address, subject, and content
    <details>
    <summary> Show example </summary>
    
    </details>

### Adding Attachments
- To include attachments with the email, click on the attachment icon or 
look for an “Choose File” button
    <details>
    <summary> Show example </summary>
    
    </details>

### Inbox and Viewing
- The inbox provides separate viewing modes for sent and received emails
- To view an email, click on it from the list in the inbox
- Clicking on an email will allow you to view its contents, including the 
sender, subject, and message
    <details>
    <summary> Show example </summary>
    
    </details>
### Deleting Emails
- To delete an email, first, view its contents by clicking on it
- Within the email view, locate the "Delete Email" button
- Clicking the "Delete Email" button will remove the email from your view 
and potentially move it to a designated trash or deleted items folder
    <details>
    <summary> Show example </summary>
    
    </details>
</details>

<details>
<summary> Chat Management </summary>





</details>
<details>
<summary>ToDo List Management</summary>
This section covers the management of the To-Do List feature. Here are the 
instructions for each action:

### Adding Items
- On the left side of the email page, locate the dedicated section for the 
To-Do List
- Fill out the task description and due date fields
- Press the "+" button to add the task to the list
    <details>
    <summary> Show example </summary>
    
    </details>

### Marking Off Items
- To mark a task as done, simply click on the task in the list
- The task will be visually indicated as completed
    <details>
    <summary> Show example </summary>
    
    </details>

### Deleting items
- Each task in the list will have an "x" button next to it
- Clicking the "x" button will delete the corresponding task from the list
    <details>
    <summary> Show example </summary>
    
    </details>

### Editing Items
- Next to each task in the list, there is an edit button.
- Clicking the edit button will activate the task's edit mode.
- In edit mode, you can modify the task's description and due date.
- To save the changes, click the edit button again, and the task will exit 
edit mode.
    <details>
    <summary> Show example </summary>
    
    </details>
</details>
