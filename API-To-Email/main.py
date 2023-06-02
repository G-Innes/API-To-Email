import os
import ssl
import sys
import smtplib
from ski import ski_api
from meme import meme_api
from dotenv import load_dotenv
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError


# Main function calls arguments to validate length & assign to variables,
# Conditionals call relevant API functions & send_email function is called with relevant arguments
# If not valid API name, program exits
def main():
    recipient, api = arguments()
    load_dotenv()
    api_key = os.getenv("api_key")
    email_password = os.getenv("email_password")

    if api == "meme":
        print("Valid API!✅")
        content = meme_api(api_key)
        send_email(recipient, email_password, content, api)
    elif api == "ski":
        print("Valid API!✅")
        content = ski_api(api_key)
        send_email(recipient, email_password, content, api)
    else:
        print("Invalid API!⛔️")
        sys.exit()

# Arguments function assigns the cmd line args to variables, checks if correct amount of args
# & runs check_email passing email address, returns both for use in Main
# returns both for use in Main
def arguments():
    if len(sys.argv) != 3:
        print("Invalid Number Of Arguments!⛔️")
        sys.exit()
    else:
        recipient = sys.argv[1]
        api = sys.argv[2]
        check_email(recipient)
        return recipient, api

# CheckEmail validates email address using library function & try/except block
# If not valid email error message is printed to user & program exits
def check_email(recipient):
    try:
        validate_email(recipient)
        result = "Valid Email!✅"
        print(result)
        return result
    except EmailNotValidError as e:
        raise e

# Send Email is called from Main with the relevant variables & assigns to the body of the email & sets subject depending on API choice
# variables unpacked from content (ski) in order to arrange select data with loops before assigning to email body
def send_email(recipient, email_password, content, api):
    sender = "Your Personal Gmail account goes here"
    password = email_password
    subject = ""
    body = ""

    if api == "meme":
        subject = "A Random Programming Meme"
        body = f'Here is your random programming meme:<br><br><img src="{content}" alt="Meme"><br><br> Re-run the program for another one!'

    elif api == "ski":
        subject = "Whistler Ski Info"
        name, website, conditions, lift_status, user, tweets = content

        # using list comp, formats dict to string of key value pairs & joins each with a new line
        conditions_formatted = "\n".join([f"{key}: {value}" for key, value in conditions.items()])

        # using a while loop i iterates over each KV pair in the lift_status dict, ensuring all KV pairs are included
        # column is created by slicing lift_status using list/items methods & selects a portion of key value pairs per column
        # for loop iterates over each KV pair in column & appends it to the colummn_formatted list
        # lift_status_formatted then joins the formatted strings together with seperators, creating a single string representing the current column
        lift_status_formatted = ""
        column_rows = 7
        i = 0
        while i < len(lift_status):
            column = list(lift_status.items())[i : i + column_rows]
            column_formatted = []
            for lift, status in column:
                column_formatted.append(f"{lift}: {status}")
            lift_status_formatted += "\n".join(column_formatted) + "\n\n"
            i += column_rows

        # tweet iterates over each itme in tweets dict, assigning the value of the text & created at keys
        # text & created_at are formatted into a string & appended to the tweets_formatted string & loops until all tweets are included
        tweets_formatted = ""
        for tweet in tweets:
            text = tweet["text"]
            created_at = tweet["created_at"]
            tweets_formatted += f"Tweet: \n{text}\nCreated: {created_at}\n{'-' * 100}\n"

        body = f"Resort Name: {name}\nWebsite: {website}\n\nConditions: \n{conditions_formatted}\n\nLift Status:\n {lift_status_formatted}\n\nRecent Tweets From {user}:\n\n {tweets_formatted}"

    # creates an empty email message object from email.message module
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject

    # Sets the email subtype to HTML to display the image within the email itself (plain if ski api) & includes the body content
    email.set_content(body, subtype="html" if api == "meme" else "plain")

    # creates a default SSL context for establishing a secure connection
    context = ssl.create_default_context()

    # establishes connection to SMTP.gmail server over secure SSL connection on port 465.
    # login method is used to authenticate with the server using the email & password.
    # sendmail method is called to send the email, with the senders email, recipient's email & the message converted to a string
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email.as_string())

if __name__ == "__main__":
    main()
