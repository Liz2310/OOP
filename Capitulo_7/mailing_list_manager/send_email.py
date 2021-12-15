"""The manager will keep track of email addresses categorized into named groups.
When it's time to send a message, we can pick a group and send the message to
all email addresses assigned to that group.

We ought to have a safe way to test it, without sending emails to a bunch of
real people. Luckily, Python has our back here; like the test HTTP server, it
has a built-in Simple Mail Transfer Protocol (SMTP) server that we can instruct
to capture any messages we send without actually sending them. We can run the
server with the following command:
   $python -m smtpd -n -c DebuggingServer localhost:1025

Running this command at command prompt will start an SMTP server running on
port 1025 on the local machine. But we've instructed it to use the DebuggingServer
class (this class comes with the built-in SMTP module), which, instead of sending
mails to the intended recipients, simply prints them on the terminal screen as it
receives them.
"""

import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, *to_addrs, host="localhost",
              port=1025, headers=None):

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    headers = headers if headers else {}

    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr, addr, email.as_string())

    sender.quit()


send_email("A model subject", "The message contents","from@example.com", "to1@example.com", "to2@example.com")