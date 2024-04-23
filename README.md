# Gmail-api-email-sender
Python script using gmail API to send individual emails from a text file. User can customize the time interval between sending each email.

## Getting Started
This script is meant to be executed through Bash or in an IDE.

The only setup required is to download an OAuth 2.0 Client ID file from Google
that will authorize your application.

This can be done at: https://console.developers.google.com/apis/credentials.
For those who haven't created a credential for Google's API, after clicking the 
link above (and logging in to the appropriate account),

1. Select/create the project that this authentication is for (if creating a new 
project make sure to configure the OAuth consent screen; you only need to set 
an Application name)

2. Click on the "Dashboard" tab, then "Enable APIs and Services". Search for 
Gmail and enable.

3. Click on the Credentials tab, then "Create Credentials" > "OAuth client ID".

4. Select what kind of application this is for, and give it a memorable name.
Fill out all necessary information for the credential (e.g., if choosing 
"Web Application" make sure to add an Authorized Redirect URI. See 
https://developers.google.com/identity/protocols/oauth2 for more infomation).

5. Back on the credentials screen, click the download icon next to the 
credential you just created to download it as a JSON object.

6. Save this file as "client_secret.json" and place it in the root directory of 
your application. (The `Gmail` class takes in an argument for the name of this 
file if you choose to name it otherwise.)

## Installation

Install using `pip` (Python3).

```bash
pip3 install simplegmail
```


The first time you create a new instance of the `Gmail` class, a browser window 
will open, and you'll be asked to give permissions to the application. This 
will save an access token in a file named "gmail-token.json", and only needs to 
occur once.

Special thanks to [@jeremyephron](https://github.com/jeremyephron) for the set up instructions.


## How to
Create a `.txt` file with your list of emails to contact in the same directory as the python script.
Make sure each email address starts on a new line.
If not use bash command (make sure you are in the correct directory) : 
```bash
tr ' ' '\n' < originalfile.txt > newfile.txt
```

Set the amount of time you want to have pass between each sending depending on daily limits, hourly limits etc... (see comments in script)

execute script :
```bash
python gmailsender.py
```

or 

```bash
python3 gmailsender.py
```



