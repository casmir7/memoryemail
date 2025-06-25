import smtplib
import json
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

DATA_FILE = "future_messages.json"

def add_message():
    email = input("Your Email: ")
    message = input("Message to Future You: ")
    send_date = (datetime.today() + timedelta(days=365)).strftime("%Y-%m-%d")

    entry = {
        "email": email,
        "message": message,
        "send_date": send_date
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            messages = json.load(f)
    else:
        messages = []

    messages.append(entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

    print(f"✅ Message saved! It will be delivered on {send_date}.")


def send_due_messages():
    today = datetime.today().strftime("%Y-%m-%d")
    if not os.path.exists(DATA_FILE): return

    with open(DATA_FILE, 'r') as f:
        messages = json.load(f)

    remaining = []
    for msg in messages:
        if msg['send_date'] == today:
            try:
                send_email(msg['email'], msg['message'])
                print(f"📬 Sent message to {msg['email']}")
            except Exception as e:
                print(f"❌ Failed to send to {msg['email']}: {e}")
                remaining.append(msg)
        else:
            remaining.append(msg)

    with open(DATA_FILE, 'w') as f:
        json.dump(remaining, f, indent=2)


def send_email(to_email, message_body):
    # === SMTP DETAILS ===
    from_email = "your.email@example.com"
    password = "your_app_password"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "A message from your past self ✉️"

    msg.attach(MIMEText(message_body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)

# === RUN THIS FILE ===
print("1. Add a future message (auto 1 year ahead)")
print("2. Send any due messages")
choice = input("Choose (1 or 2): ")

if choice == '1':
    add_message()
elif choice == '2':
    send_due_messages()
else:
    print("Invalid option.")
