# Project Title: Phishing Simulation and Awareness Tool

## Description
This tool is designed to simulate phishing attacks and educate users about identifying and avoiding phishing attempts. By providing real-world-like scenarios, it enhances awareness and understanding of phishing tactics.

## Features
- Simulated phishing emails with realistic fake login pages.
- Educational email feedback for users who interact with the phishing page.
- Logging and tracking user interactions to analyze behavior.
- Developed using Flask, SQLite, and Python, with email functionality via SMTP.

## How It Works
1. A phishing email is sent to the user with a link to a fake login page.
2. If the user interacts with the page (e.g., entering credentials), the interaction is logged in the SQLite database.
3. An educational email is sent to the user, explaining phishing techniques and prevention tips.
4. User actions are stored in the database for analysis.

## Prerequisites
- Python 3.8 or above.
- Dependencies listed in `requirements.txt`.

## Installation
```bash
# Clone this repository
git clone <repository-url>

# Navigate to the project directory
cd <repository-name>


# Install dependencies
pip install -r requirements.txt

#Set up the .env file with the following variables:
EMAIL_USER=<your-email-address>  
EMAIL_PASS=<your-email-password>  

#Run the application:
python app.py
```
## Features
- app.py: The main application script hosting the phishing page and logging user interactions.
- templates/: Contains HTML files (index.html and hack.html).
- static/: CSS and other static files.
- requirements.txt: Lists the required Python packages.
- .env: Contains email credentials for SMTP (not included in the repo; add it manually).
- .gitignore: Ensures sensitive files like .env are excluded.

