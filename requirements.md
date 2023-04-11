
## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login/Logout Page
2. Register User
3. Send Email
4. Send Messages through Chat
5. Search for Emails
6. Reply to Email
7. Send Emojis
8. Creating todo list
9. Add items to todo list
10. Mark off completed items on todo list
11. Filtering/Sorting Emails
12. Deleting Email
13. Set Notification Setting (do not disturb/online)

## Non-functional Requirements

1. Must have an interactive UI
2. Have a noise notification when email is received
3. non-functional
4. non-functional

## Use Cases

1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

1. Login User 
- **Pre-condition:** User must have an account, user must be on the homepage 

- **Trigger:** User presses login page redirect button

- **Primary Sequence:**
  
  1. User is directed to login page
  2. User types in account username
  3. User types in account pasword
  4. User presses log-in button
  5. Database logs the user in
  6. App redirects user to homepage

- **Primary Postconditions:** User receives confirmation message. User is logged in and able to use the app.

- **Alternate Sequence:** 
  
  1. User fails to login 3 times.
  2. Message displays saying that 2 more attempts and account will be locked for 10 minutes.
  3. User fails to login 2 more times.
  4. Message displays saying that account is locked, button saying "Go back to home" is also displayed.


2. Register User
- **Pre-condition:** User does not have an existing account
  
- **Trigger:** User selects "Register" button
  
- **Primary Sequence:**
  
  1. Page directs user to a registration page asking for user’s full name, email address and 
password
  2. User enters full name
  3. User creates an email address
  4. User creates a password 
  5. User selects Create Account

- **Primary Postconditions:** 

  1. User successfully creates a new account
      * Page directs to log in page
      * System allows User to log in with an email address and password
  2. User did not create an account
      * System did not save data
      * User cannot login with their email and password

- **Alternate Sequence:**
  
  1. System checks data and finds that there is an existing account with the entered email 
address
      * System displays an notifying the user that there’s an existing account 
      * System prompts user to enter another email address
  
3. Send Email
- **Pre-condition:** User is registered and logged into web application
  
- **Trigger:** User selects "Compose" button
  
- **Primary Sequence:**
  
  1. System prompts user to enter recipient(s) email address, email subject, and 
messages/attachments
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

5. Search for Email(s)
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
  
6. Reply to Email
- **Pre-condition:** User must be logged in and have an email (from a recipient) to reply to
  
- **Trigger:** User clicks and opens the email they want to reply to
  
- **Primary Sequence:**
  
  1. User clicks on the "reply" button
  2. System opens up a compose window with the recipient's name/email address in the "To" field
  3. User types their reply in the body of the email
  4. User clicks the "send" button to send the email
  5. System sends the email to the recipient

- **Primary Postconditions:**

  1. The user successfully sends the reply and the recipient receives the email
  2. User's reply mail is added/saved under a "Sent" folder

- **Alternate Sequence:**
  
  1. User decides to cancel the reply
       * User clicks cancel button or the "x" button to close the window
       * System sends a confirmation message to user wanting to cancel the reply
       * User confirms and system exits user out of the window

 9. Create to-do list

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

10. Add items to to-do list

- **Preconditions:** The user is logged into an account, the user is on the lists page, there is an existing list in the account

- **Trigger:** The user clicks on a list to edit it

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


13. Set Notification Settings

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
