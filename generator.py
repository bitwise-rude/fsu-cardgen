# Written and Maintained by The Automation Team - FSU
# Meyan, Aaditya , Avi

import csv
from PIL import Image, ImageDraw, ImageFont
import os

TEMPLATE_PATH = "data/template.png"
CSV_PATH = "data/data.csv"
OUTPUT_DIR = "output"
FONT_PATH = "data/font.ttf"
FONT_SIZE = 60
TEXT_COLOR = (20, 35, 60) 
Y_POSITION = 780  


os.makedirs(OUTPUT_DIR, exist_ok=True)

template = Image.open(TEMPLATE_PATH)

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        full_name = row["fullName"].strip()
        roll_no = row["classRollNo"].strip()

        image = template.copy()
        draw = ImageDraw.Draw(image)

        bbox = draw.textbbox((0, 0), full_name, font=font)
        text_width = bbox[2] - bbox[0]

        image_width = image.width
        x_position = (image_width - text_width) // 2

        draw.text(
            (x_position, Y_POSITION),
            full_name,
            font=font,
            fill=TEXT_COLOR
        )

        output_path = os.path.join(OUTPUT_DIR, f"{roll_no}.png")
        image.save(output_path)

        print(f"Generated: {output_path}")

print("Done generating all invitations.")

