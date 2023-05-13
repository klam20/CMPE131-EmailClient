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
This section covers the various actions related to managing user 
accounts. 
Here are the instructions for each:

### Registration (Nicole)
- To register for an account, go to the home page and click the “Sign-up” 
button
- Create an email address and password to complete registration
    <details>
    <summary> Show example </summary>
    <img width="166" alt="Screen Shot 2023-05-11 at 9 23 06 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/983ceda8-ba50-4d6e-ac7a-9ccf7aaede4b">
    <img width="591" alt="registration" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/7cdb752b-2db1-4d98-a37f-34c50933f121">
    </details>

### Logging In (Jeffrey)
- Once you have a registered account, use the login feature to access 
other functionalities.
- Enter your registered email and password to log in
    <details>
    <summary> Show example </summary>
    <img width="166" alt="Screen Shot 2023-05-11 at 9 23 06 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/5330893d-a699-4e31-8fb0-9892a9bb6707">
    <img width="715" alt="login" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/4ef2547a-2a7a-4e1c-bbb7-8d627127ab8b">
    </details>

### Logging Out (Jeffrey)
- To log out, locate the "Log-out" button in the navigation bar and click 
on it
- Logging out will terminate your current session
    <details>
    <summary> Show example </summary>
    <img width="106" alt="Screen Shot 2023-05-11 at 9 24 43 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/d4ab372c-bbad-439b-90c5-77db189bbd39">
    </details>

### Deleting Account (Jeffrey)
- If you wish to delete your account, find the "Delete Account" button in 
the navigation bar.
- Click on the button to initiate the account deletion process
    <details>
    <summary> Show example </summary>
    <img width="143" alt="Screen Shot 2023-05-11 at 9 25 47 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/2c56c947-dc28-49dc-bb45-b90ce2409805">
    </details>
</details>

<details>
<summary> Email Management</summary>
This section provides instructions for managing emails within the 
application. Here are the instructions for each action:

### Compose Button (Nicole)
- Locate the compose button on the bottom right corner
- Click on the compose button to create and send emails
    <details>
    <summary> Show example </summary>
    <img width="106" alt="Screen Shot 2023-05-11 at 9 26 13 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/140209d6-4008-4054-bd25-a2881ee21f41">
    </details>

### Filling out the Form (Nicole)
- To send an email, provide the required information such as the 
recipient's email address, subject, and content
    <details>
    <summary> Show example </summary>
    <img width="363" alt="Screen Shot 2023-05-11 at 9 26 42 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/26f40087-e432-4ff9-9b24-855abeb37d3a">
    </details>

### Adding Attachments (Jeffrey)
- To include attachments with the email, click on the attachment icon or 
look for an “Choose File” button
    <details>
    <summary> Show example </summary>
    <img width="332" alt="Screen Shot 2023-05-11 at 9 31 16 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/54def0c8-dae6-4746-8b97-cdb839cc651e">
    </details>

### Inbox and Viewing (Jeffrey)
- The inbox provides separate viewing modes for sent and received emails
- To view an email, click on it from the list in the inbox
- Clicking on an email will allow you to view its contents, including the 
sender, subject, and message
    <details>
    <summary> Show example </summary>
    <img width="637" alt="Screen Shot 2023-05-11 at 9 32 27 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/adb39945-9dd2-45b5-be48-4fd64adc7a69">
    <img width="605" alt="Screen Shot 2023-05-11 at 9 32 36 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/25e522cb-01f8-4ba6-8d4e-257705d9a395">
    </details>
    
### Search Bar (Bryant)
- To search an email, first, click on the search bar
- Then the user inputs text that they want search within their existing emails
- Clicking the submit will prompt the system to search based on user input
- Then, the user can click on "received" or "sent" to see emails that matched the input
  <details>
  <summary> Show example </summary>
  <img width="600" src="https://github.com/klam20/CMPE131-EmailClient/assets/77865786/f0fa14a7-b13c-4e8b-b00b-a64c195090bc">
  </details>

### Deleting Emails (Jeffrey)
- To delete an email, first, view its contents by clicking on it
- Within the email view, locate the "Delete Email" button
- Clicking the "Delete Email" button will remove the email from your view 
and potentially move it to a designated trash or deleted items folder
    <details>
    <summary> Show example </summary>  
    <img width="510" alt="Screen Shot 2023-05-11 at 9 34 08 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/9feccf1b-2e1d-499d-8384-15930d501c67">
    </details>
</details>

<details>
<summary> Chat Management </summary>
This section covers the management of chat messages within the application. Here are the 
instructions for each action:

### Create Messages (Bryant)
- By selecting the create message button, you can enter the user you want to message
- You then select the conversation slot with the user’s email address
- Type message in the input field and press send to see your message displayed in the 
chat window
    <details>
    <summary> Show example </summary>
    <img width="396" alt="Screen Shot 2023-05-11 at 9 35 14 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/5b526e57-cdad-4da0-a2df-b2d15521c118">
    <img width="235" alt="Screen Shot 2023-05-11 at 9 35 18 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/8849617d-c198-49b1-a10a-c17e9513e532">
    </details>
### Delete Messages and Conversations (Bryant)
- You are able to delete messages and will be no longer visible to the other participant
    <details>
    <summary> Show example </summary>
    <img width="396" alt="Screen Shot 2023-05-11 at 9 35 14 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/2341f4e1-6f3c-474e-886b-549954fdb457">
    </details>

</details>

<details>
<summary>ToDo List Management</summary>
This section covers the management of the To-Do List feature. Here are the 
instructions for each action:

### Adding Items (Anthony)
- On the left side of the email page, locate the dedicated section for the To-Do List
- Fill out the task description and due date fields
- Press the "+" button to add the task to the list
    <details>
    <summary> Show example </summary>
    <img width="460" alt="Screen Shot 2023-05-11 at 9 38 56 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/f2e50f73-a7d0-47b3-b976-ab142db346fc">
    </details>

### Marking Off Items (Anthony)
- To mark a task as done, simply click on the task in the list
- The task will be visually indicated as completed
    <details>
    <summary> Show example </summary>
    <img width="471" alt="Screen Shot 2023-05-11 at 9 39 02 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/fbdaf643-2a5c-4824-8900-185028ee2c43">
    </details>

### Deleting items (Anthony)
- Each task in the list will have an "x" button next to it
- Clicking the "x" button will delete the corresponding task from the list
    <details>
    <summary> Show example </summary>
    <img width="460" alt="Screen Shot 2023-05-11 at 9 38 56 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/4a662c33-73ff-4a78-8830-4fbbcde5ef4c">
    </details>


### Editing Items (Anthony)
- Next to each task in the list, there is an edit button.
- Clicking the edit button will activate the task's edit mode.
- In edit mode, you can modify the task's description and due date.
- To save the changes, click the edit button again, and the task will exit 
edit mode.
    <details>
    <summary> Show example </summary>
    <img width="460" alt="Screen Shot 2023-05-11 at 9 38 56 PM" src="https://github.com/klam20/CMPE131-EmailClient/assets/125083955/5b9b670c-7308-49a7-a5bf-a4140cb6fbe8">
    </details>

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
