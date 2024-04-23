from simplegmail import Gmail
import time

gmail = Gmail()  # will open a browser window to ask you to log in and authenticate

params = {
  "sender": "YourEmailAddress@gmail.com",
  "subject": "My first email",
  "msg_html": "" # or use "msg_plain" for plain text if no special formatting required

}

# read the file
with open ('Path/to/email/list.txt', 'r') as file :
  emails = file.readlines()

# Send emails to each address
for email in emails :
  email = email.strip()
  params["to"]= email
  try :
    message = gmail.send_message(**params)
    time.sleep(4)        # adjust seconds as needed
    print(f'email sent to {email}')
  except:
    print(f"{email} REJECTED") # if an email is not formatted correctly this message will appear


