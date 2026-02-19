import csv
from PIL import Image, ImageDraw, ImageFont
import os

# ===== CONFIG =====
TEMPLATE_PATH = "template.png"
CSV_PATH = "data.csv"
OUTPUT_DIR = "output"
FONT_PATH = "PlayfairDisplay-Bold.ttf"  # Change if different
FONT_SIZE = 60
TEXT_COLOR = (20, 35, 60)  # Deep elegant navy
Y_POSITION = 780  # <-- Adjust this only

# ==================

# Make output folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load template once
template = Image.open(TEMPLATE_PATH)

# Load font
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        full_name = row["fullName"].strip()
        roll_no = row["classRollNo"].strip()

        # Copy template for each student
        image = template.copy()
        draw = ImageDraw.Draw(image)

        # Calculate text width
        bbox = draw.textbbox((0, 0), full_name, font=font)
        text_width = bbox[2] - bbox[0]

        # Center horizontally
        image_width = image.width
        x_position = (image_width - text_width) // 2

        # Draw text
        draw.text(
            (x_position, Y_POSITION),
            full_name,
            font=font,
            fill=TEXT_COLOR
        )

        # Save file as roll number
        output_path = os.path.join(OUTPUT_DIR, f"{roll_no}.png")
        image.save(output_path)

        print(f"Generated: {output_path}")

print("Done generating all invitations.")

