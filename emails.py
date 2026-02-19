# Written by Aadi, sabotaged by Meyan 

# ------------------------------
#             Imports
# ------------------------------

import smtplib
import time
import os
from email.message import EmailMessage

# ---------------------------
#           Constants
# ---------------------------

SMTP_SERVER = "smtp.gmail.com"   
SMTP_PORT = 587

EMAIL_ADDRESS = "081bct002.aaditya@pcampus.edu.np"
EMAIL_PASSWORD = ""

DELAY_SECONDS = 1
MAX_EMAILS = 1500

sent_count = 0


# Server things
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

def send_mail(rollno:str,firstname:str,email:str) -> None:
        ''' Sends Mail to the specified rollno, firstname and email '''

        global sent_count

        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email
        msg["Subject"] = "Invitation to the Annual General Meeting organized by the Free Students’ Union, Pulchowk Campus - 2081."

        msg.set_content(f"""
Dear {firstname},
            We are honored to invite you to the Annual General Meeting (AGM) organized by the Free Students’ Union, Pulchowk Campus - 2081, scheduled to be held on 9th Falgun, 2082, at the Library Hall, Pulchowk Campus.

Your presence at this gathering will be highly valued as we reflect on the Union’s achievements over the past year, present the annual progress report, and engage in discussions on the future direction of our student body. The AGM will also include a certificate distribution ceremony to acknowledge the dedication and contributions of our members.

We sincerely hope you will join us and help make this event a meaningful occasion. Your participation will be greatly appreciated.

Warm regards,
Free Students’ Union, Pulchowk Campus - 2081
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
