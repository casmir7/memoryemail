

# 🕰️ Time-Locked Message Sender (Ritual Memory System)

This is a Python-powered tool that lets you send a message to your future self — exactly one year from the day you wrote it.

Inspired by West African oral traditions where wisdom was preserved through timing, ritual, and repetition, this system reimagines memory as an act of code. Some messages are not for now — they are for the you that survives.

---

## ⚙️ SMTP Configuration

Edit `ritual_memory.py` and update your email credentials here:

```python
from_email = "your.email@example.com"
password = "your_app_password"  # Use Gmail App Password
smtp_server = "smtp.gmail.com"
smtp_port = 587

👉 For Gmail, you must enable 2FA and create an App Password.

⸻

▶️ How to Run the Script

Run this manually from the terminal:

python ritual_memory.py

You’ll see:

1. Add a future message (auto 1 year ahead)
2. Send any due messages
Choose (1 or 2):

	•	Choosing 1 will prompt for:
	•	Your email
	•	A personal message
	•	(Date is auto-generated: one year from today)
	•	Choosing 2 will check for and send any messages due today.

⸻

📝 Sample JSON Entry

After you add a message, the script saves it in future_messages.json:

[
  {
    "email": "kojo@example.com",
    "message": "You survived. That’s enough.",
    "send_date": "2025-06-25"
  }
]

Each entry is private and delivered only to its recipient.

⸻

🔁 Automate Delivery with Cron (Linux/macOS)

Let the script run daily and automatically deliver messages.

Step 1: Open your crontab

crontab -e

Step 2: Add this line

Runs the script every day at 7 AM and triggers Option 2 (send due messages):

0 7 * * * /usr/bin/python3 /full/path/to/ritual_memory.py <<EOF
2
EOF

📌 Replace /full/path/to/ritual_memory.py with the actual location of your file.
📌 Find your Python path using:

which python3

Optional: Add error logging

0 7 * * * /usr/bin/python3 /full/path/to/ritual_memory.py <<EOF
2
EOF
2>> /tmp/ritual_errors.log



⸻

📋 Requirements
	•	Python 3.x
	•	Gmail or SMTP-enabled email account
	•	App Password if using Gmail (for secure authentication)

🛠️ This tool has no external dependencies — it uses only Python’s standard library.

⸻

📦 Project Files

File	Description
ritual_memory.py	Main script
future_messages.json	Local storage of messages
README.md	Full documentation (you are here)



⸻

🔮 Future Ideas
	•	🔐 Add Fernet/AES encryption for private messages
	•	🌕 Allow date targeting based on lunar or seasonal cycles
	•	🧍‍♂️ Contributor system (group rituals, community archives)
	•	📬 HTML-based message formatting
	•	🌐 Web-based submission form and time viewer

⸻

💡 Why This Matters

In traditional West African memory systems, rituals, rhythms, and repetition kept data alive. This project revives that mindset using code. Messages aren’t just stored — they arrive when you most need them, not when you wrote them.

“What you write today could become your future medicine.”

⸻

📜 License

MIT License — share freely, remix, and build your own rituals.

---
