import smtplib
import os
from email.message import EmailMessage
from pathlib import Path


class EmailSender:
    def __init__(self):
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")

        if not self.email_user or not self.email_password:
            raise ValueError("EMAIL_USER and EMAIL_PASSWORD must be set as environment variables.")

    def send_email_with_attachment(self, subject, body, recipients, attachment_path):
        msg = EmailMessage()
        msg["From"] = self.email_user
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.set_content(body)

        attachment_path = Path(attachment_path)

        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = attachment_path.name

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name,
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.email_user, self.email_password)
            smtp.send_message(msg)

        print("Email sent successfully!")