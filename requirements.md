## Functional Requirements

1. Login/Logout Page
2. Register User
3. Send Email
4. Send Messages through Chat
5. Search for Emails
6. Add reactions to chat messages
7. Creating todo list
8. Add items to todo list
9. Mark off completed items on todo list
10. Filter Emails by Category (date,alphabetic,unread)
11. Deleting Email
12. Set Notification Setting (do not disturb/online)

## Non-functional Requirements

1. Must have an interactive UI
2. Have a noise notification when email is received

## Use Cases

1. Login User (Jeffrey)
- **Pre-condition:** User must have an account, user must be on the homepage 

- **Trigger:** User presses login page redirect button

- **Primary Sequence:**
  
  1. User is directed to login page
  2. User types in account username
  3. User types in account password
  4. User presses log-in button
  5. App redirects user to homepage on success

- **Primary Postconditions:** User receives confirmation message. User is logged in and able to use the app.

- **Alternate Sequence:** 
  
  1. Incorrect password or username entered
      * Display message "incorrect username or password entered"
      * Clear username and password text-boxes
      * User will not be logged in


2. Register User (Nicole)
- **Pre-condition:** User does not have an existing account
  
- **Trigger:** User selects "Register" button
  
- **Primary Sequence:**
  
  1. Page directs user to a registration page
  2. User enters full name
  3. User creates an email address
  4. User creates a password 
  5. User selects Create Account

- **Primary Postconditions:** 

  1. User successfully creates a new account
      * Page directs to log in page
      * System allows User to log in with an email address and password
      
- **Alternate Sequence:**
  
  1. System checks data and finds that there is an existing account with the entered email 
address
      * System displays an notifying the user that there’s an existing account 
      * System prompts user to enter another email address
  
3. Send Email (Nicole)
- **Pre-condition:** User is registered and logged into web application
  
- **Trigger:** User selects "Compose" button
  
- **Primary Sequence:**
  1. A compose message box opens
  2. User enters recipient(s) email address
  3. User enters an email address
  4. User enters a message or adds an attachment in the email body
  5. User selects “send” button

- **Primary Postconditions:**

  1. User sends an email
       * Recipient receives email
       * System categories email as sent
  2. User does not send an email
       * Recipeint does not receive email

- **Alternate Sequence:**
  
  1. User did not enter a email address, subject line, or message
       * System does not allow email to be sent
       * System prompts user to fill up the missing information
  2. User did not enter a valid/existing email address
       * System displays an error message to user
       * System prompts user to enter a valid email address

5. Search for Email(s) (Bryant)
- **Pre-condition:** User must be logged in and has preexisting emails
  
- **Trigger:** User clicks the search box
  
- **Primary Sequence:**
  
  1. System prompts the user to search
  2. User types into the search box (using keywords or names)
  3. User presses enter to prompt the system to search
  4. System pops up recommended emails based on user input

- **Primary Postconditions:**

  1. The user can view emails that matched their search criteria
  2. The user can interact with the displayed emails

- **Alternate Sequence:**
  
  1. The user does not have emails that matched the input
       * System displays message to user that there are no emails that matched the input
       * System allows user to revise the text or clear the search box
       * User refines their search to perform a new search
       * User presses enter to prompt the system to search
       * System displays new recommended emails based on the new search
  2. The system takes a long time to complete the search
       * User can wait for it to complete or cancel the search
       * The system displays a progress bar to show the loading status of the search
       * If the loading cannot complete, the system displays an error message
  
4. Send Messages through Chat (Bryant)
- **Pre-condition:** User must be logged in
  
- **Trigger:** User clicks chat button
  
- **Primary Sequence:**
  
  1. Enter email of person you want to message
  2. Press Start Chat button
  3. Open a chat box with the recipient email auto-filled
  4. Type your message
  5. User clicks the "send" button to send the message

- **Primary Postconditions:**

  1. The user successfully sends the message and the recipient receives the messages
  2. Message should display on both sender and receiver chat-history
  3. The chat-box must stay open

- **Alternate Sequence:**
  
  1. User presses Start Chat button with an invalid email
       * Have a text-box display stating that the email is invalid
       * Gray out the Start Chat button until a new email is inserted

 7. Create to-do list (Anthony)

- **Predconditions:** User must be logged into an account, the user is on the lists page

- **Trigger:** The user clicks a "Create new list" button

- **Primary Sequence:**

  1. The client displays a prompt that asks for the user to input list name and tasks with their due date.
  2. The user enters the name of the list
  3. The user enters the names of the tasks and their due dates
  4. The user clicks a “make list” buttons
  5. The lists with the name and desired tasks inside are created
  6. The new list is added to the lists page
  7. The user is taken back to the lists page

- **Primary Postconditions:**

  1. User has created a todo list with the desired tasks
  2. The list is displayed on the lists page and usable

- **Alternative Sequence:**

  1. The user decides to not make the list
       * The user clicks an x button at the top of the input box
       * The input box erases all of the given inputs up to that point
       * The input box is closed
       * The user is taken back to the lists page

8. Add items to to-do list (Anthony)

- **Preconditions:** The user is logged into an account, the user is on the embedded list section, there is an existing list in the account

- **Trigger:** The user clicks on an existing list

- **Primary Sequence:**

  1. The user clicks on a edit button
  2. The user is prompted to enter a new task and its due dates
  3. The user enters the task name and due date
  4. The user clicks an add task button
  5. The task is added to the list
  6. The text inputs are cleared and the user is able to add more tasks if desired
  7. When the user is done adding tasks the user clicks a save button
  8. The user is taken back to the lists page

- **Primary Postconditions:**

  1. The new tasks are added to the existing list
  2. The new tasks are displayed then the list is selected

- **Alternative Sequence:**

  1. The user decides to not add tasks
       * The user clicks an x button at the top of the input box
       * The input box erases all of the given inputs up to that point
       * The input box is closed
       * The user is taken back to the lists page


12. Set Notification Settings (Jeffrey)

- **Preconditions:** User must have an account, user must bein their email home

- **Trigger:** User presses notifcation setting pull-down bar

- **Primary Sequence:**

  1. User presses do not disturb option in the pull-down menu
  2. A prompt will display 1) textbox asking user how long they want to stay in do-not-disturb 2) a pull-down bar inside the textbox which is used to select length of time
  3. User will press the pull-down bar inside the prompt
  4. User will select time options that are between 30 minutes - 2 hrs in 30 minute increments, OR choose an option to keep do not disturb on until deactivated
  5. User presses OK button after filling all details
  6. Email client mutes notification sounds based on user's requrest/details provided
  7. Redirect to email home

- **Primary Postconditions:**
  1. Email client is set to mute any incoming emails/messages

- **Alternative Sequence:**

  1. User chooses online mode instead of do not disturb
  2. User presses OK button
  3. Email client enables notification sounds
