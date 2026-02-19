# Written by Aadi, sabotaged by Meyan 

import smtplib
import csv
import time
import os
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"   
SMTP_PORT = 587

EMAIL_ADDRESS = "081bct002.aaditya@pcampus.edu.np"
EMAIL_PASSWORD = ""

DELAY_SECONDS = 1
MAX_EMAILS = 1500

sent_count = 0

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

def send_mail(rollno,firstname,email):
        global sent_count

        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email
        msg["Subject"] = "Invitation to Annual General Meeting."

        msg.set_content(f"""
Dear {firstname},
                        """)

        image_path = f"output/{rollno}.png"

        if not os.path.exists(image_path):
            print(f"Missing image: {image_path}")
            return

        with open(image_path, "rb") as img:
            msg.add_attachment(
                    img.read(),
                    maintype="image",
                    subtype="jpeg",
                    filename=os.path.basename(image_path)
                    )

        try:
            server.send_message(msg)
            sent_count += 1

            with open("sent_log.txt", "a") as log:
                log.write(f"{email} SENT\n")

            print(f"Sent to {email}({sent_count})")
            time.sleep(DELAY_SECONDS)

        except smtplib.SMTPException as e:
            print("SMTP ERROR — STOPPING:", e)
            return
server.quit()
