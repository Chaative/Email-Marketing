import smtplib
import ssl
import csv

smtp_server = "smtp.gmail.com"
port = 465

sender_email = "example@gmail.com"
password = "example_password"

subject = "Email Marketing Campaign"
body = "Insert body of email here"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    with open('emails.csv') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for email in reader:
            receiver_email = email[0]
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, receiver_email, message)

print("Emails Sent Successfully!")