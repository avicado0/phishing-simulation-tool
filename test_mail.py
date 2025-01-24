import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gmail account details
sender_email = os.getenv('EMAIL_USER')  # Replace with the new email
app_password = os.getenv('EMAIL_PASS')  # Replace with the email password

# sender_email = "toolforgehub@gmail.com"  # Replace with your Gmail address
# app_password = "jluzaaiimnpdqnty"      # Replace with your generated app password

recipient_email = "anushkabagade23@gmail.com"


print(f"Loaded email: {sender_email}, password: {app_password}")

if sender_email is None or app_password is None:
    print("Environment variables are not loaded properly.")
    exit()

# Email content
subject = "Test Email 69"
body = "This is a test email sent using Gmail's SMTP with App Password."

message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email

# Send email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Test email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
