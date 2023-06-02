# API To Email
The API To Email project is a Python program that fetches information from 2cdifferent APIs and sends the retrieved data to a specified email address.

## Table of Contents
- [Project Description](#project-description)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Features](#features)
- [Limitations](#limitations)
- [Testing](#testing)
- [Project Requirements](#project-requirements)
- [Troubleshooting](#troubleshooting)
- [My VScode Keybinds](#my-vscode-keybinds)


## Project Description:
The program accepts 2 command line arguments- email address & the chosen API ('ski' or 'meme') & is validated in arguments()
The email address is validated using the email_validator library in check_email()
The program uses a .env file to securely store the API keys and email password. In the .env file template provided you will need to enter your personal API key from RapidAPI.com and also subscribe to the 2 API's (Link here). You will need to edit the code to use your own gmail address for the sender and also the 16 character password will need to be updated in the .env file also. (Contact me for further support if needed)
The API entered is validated and if not one of the 2 choices the program exits
After the API is called the data is formatted into a human-readable message & sent to the email address provided using Pythons built in SMPLIB library.

## Dependencies:
Built in (no installation required):

```os, ssl, sys, smtplib, email.message```

External (installation required using pip): 

```dotenv (or 'python-dotenv'), email_validator, requests, random, pytest```

## Usage:
To use the program clone the repo to your machine:

```git clone git@github.com:TuringCollegeSubmissions/ginnes-FPCS.2.git```

run the program by using:

```mail.py 'your email address' ski (or meme)```

or on some machines:

```python3 mail.py 'your email address' ski (or meme)```

## Features:
If API entered is **'meme'** then the program will call an API to fetch an image of a programming meme to be sent to the email address provided, the image is a randome choice from a list of options and should change each time the program is run.

If API entered is **'ski'** then the program call will call an API to fetch data about current ski conditions in Whistler ski resort. I have selected the information to be included in the email from the API and used various loops to arrange and display the data in a readable fashion in the message.

## Limitations:
Ski API- 10 calls per day

Meme API- 150 calls per day

## Testing:
I have included 4 unit tests: valid/invalid arguments & valid/invalid email.
run the test file using:

```pytest test-main.py```

## Project Requirements:
The program is able to accept two command line arguments

The program checks whether command line arguments are valid

The program is able to call two different APIs

The program is able to create a message based on the information retrieved from the APIs

The program is able to send an email via a Gmail account

At least three unit tests are written

At least one try/except block is used

Organization and style of the code. The code should be easy to read, with well-named functions, variables, and comments.

General understanding of sprint topics 

5 keybinds listed at the end of the submission file 

## Troubleshooting:
During implementation of SSL in the send_email function the console threw an SSL certificate verification error.

This error occurs when the SSL certificate presented by the server cannot be verified.

*This error may occur in the macOS Terminal: SSL verification error*

**To resolve this issue, you can follow these steps:**

### 1. Download the root CA certificate bundle:
```curl https://curl.se/ca/cacert.pem -o cacert.pem```

### 2. Move the downloaded cacert.pem file to a safe location on your Mac, such as /usr/local/etc/openssl/cert.pem:
**create:**
```sudo mkdir -p /usr/local/etc/openssl```

**move file:**
```sudo mv /Users/'username'/cacert.pem /usr/local/etc/openssl/cert.pem```

### 3. Set the SSL_CERT_FILE environment variable to point to the location of the cacert.pem file. Open your ~/.bash_profile or ~/.zshrc file in a text editor:
```nano ~/.bash_profile```
    **or**
```nano ~/.zshrc```

**Add the following line at the end of the file:**

```export SSL_CERT_FILE=/usr/local/etc/openssl/cert.pem```

**Save the file and exit the text editor.**

### 4. Restart your Terminal or run the source ~/.bash_profile (or source ~/.zshrc) to apply the changes.

After performing these steps, the SSL_CERT_FILE environment variable will be set to the location of the cacert.pem file

**(Feel free to send me a message in Discord regarding this if any questions)**

## My VScode Keybinds:

CMD [ or ] (indent/outdent)

CMD shift L (change all occurrences of selected)

CMD shift K (deletes current whole line)

F9 (toggle breakpoint)

CMD B (toggle explorer menu)
