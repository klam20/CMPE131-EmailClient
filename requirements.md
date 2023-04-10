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
