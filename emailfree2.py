import csv
import smtplib

# Define email parameters
sender_email = "your_email@gmail.com"
sender_password = "your_password"
subject = "Check out our new products!"
message = "Hello, we just released some awesome new products that we think you'll love. Check them out at our website!"

# Connect to the SMTP server
smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(sender_email, sender_password)

# Open CSV file of email addresses
with open('email_list.csv') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        # Send the email to each address in the list
        recipient_email = row[0]
        msg = f"Subject: {subject}\n\n{message}"
        smtp_server.sendmail(sender_email, recipient_email, msg)

# Close the SMTP server connection
smtp_server.quit()