import smtplib

# google no longer support less secure app access, this doesn't work

sender = "thehunter2807@gmail.com"
receiver = "indrabhushanjaiswar20@gmail.com"
password = "8898912128Ij@"
subject = "Mail from Python Program"
body = "This is send via python program"

#Header
message = f"""From: Hunter{sender}
To: Indrabhushan{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged In..")
    server.sendmail(sender,receiver,message)
    print("Email has been sent.")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign-in")