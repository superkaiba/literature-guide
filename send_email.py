#!/usr/bin/env python3
"""Send the daily digest email via Gmail SMTP. Called by Claude Code after generating the report."""

import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def send_digest(html_path: str):
    smtp_user = os.environ.get("SMTP_USER")
    smtp_password = os.environ.get("SMTP_PASSWORD")
    email_to = os.environ.get("EMAIL_TO", "thomasjiralerspong@gmail.com")

    if not smtp_user or not smtp_password:
        print("SMTP_USER or SMTP_PASSWORD not set, skipping email")
        sys.exit(0)

    html_content = Path(html_path).read_text()

    # Extract date from filename or content
    date_str = Path(html_path).stem

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Literature Digest — {date_str}"
    msg["From"] = smtp_user
    msg["To"] = email_to
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email_to, msg.as_string())

    print(f"Email sent to {email_to}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <html_file>")
        sys.exit(1)
    send_digest(sys.argv[1])
