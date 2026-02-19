import smtplib
import csv
import time
import os
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"      # change if Outlook
SMTP_PORT = 587

EMAIL_ADDRESS = "081bct002.aaditya@pcampus.edu.np"
EMAIL_PASSWORD = ""

DELAY_SECONDS = 1
MAX_EMAILS = 300

sent_count = 0

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

with open("falumini.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if sent_count >= MAX_EMAILS:
            print("Daily limit reached. Stopping.")
            break

        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = row["Email"]
        msg["Subject"] = "Your Invitation To Visit 17th National ASA Exhibition"

        msg.set_content(f"""
Dear {row["firstname"]},

Warm greetings from the 17th National ASA Exhibition.

We are pleased to invite you to the 17th National ASA Exhibition , an architectural exhibition organized by the Department of Architecture, Pulchowk Campus, Institute of Engineering. The exhibition will be held on 4th,5th and 6th of magh at the department of architecture.

This year’s exhibition is themed “Between Possibilities and Precision,” exploring the dynamic balance between conceptual exploration and technical rigor in architectural education and practice. The exhibited works reflect the journey from idea to execution, addressing aspects such as design intent, spatial articulation, material consideration, construction logic, and contextual response.

The exhibition will showcase a wide range of student projects, drawings, models, and installations, offering insights into contemporary architectural thinking and methodologies. It aims to serve as a platform for observation, dialogue, and shared learning among students, professionals, and visitors interested in architecture and the built environment.

We would be honored by your presence at the exhibition and highly value your engagement with the architectural discourse it seeks to present.

Warm regards,
17th National ASA Exhibition Team
Department of Architecture
Pulchowk Campus
Institute of Engineering
""")

        image_path = f"invites/{row['rollno']}.jpg"

        if not os.path.exists(image_path):
            print(f"Missing image: {image_path}")
            continue

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
                log.write(f"{row['Email']} SENT\n")

            print(f"Sent to {row['Email']} ({sent_count})")
            time.sleep(DELAY_SECONDS)

        except smtplib.SMTPException as e:
            print("SMTP ERROR — STOPPING:", e)
            break

server.quit()
