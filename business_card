import sys
import time
from waveshare_epd import epd2in13_V4  # Adjust based on your display version
from PIL import Image, ImageDraw, ImageFont
import qrcode  # To generate QR codes

# Initialize the e-Paper display
epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)

# Create a blank image (black and white)
width, height = epd.height, epd.width  # Waveshare's width/height might be swapped
image = Image.new('1', (width, height), 255)  # 1-bit, white background
draw = ImageDraw.Draw(image)

# Load a font (adjust the size for readability)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
except:
    font = ImageFont.load_default()

# Your business card details
name = "Brinae Bain"
title = "Implementation Engineer"
email = "brinae@example.com"
website = "brinaebain.com"
phone = "(123) 456-7890"

# Draw text on the image
draw.text((10, 10), name, font=font, fill=0)
draw.text((10, 30), title, font=font, fill=0)
draw.text((10, 50), email, font=font, fill=0)
draw.text((10, 70), website, font=font, fill=0)
draw.text((10, 90), phone, font=font, fill=0)

# Generate a QR code (optional)
qr = qrcode.QRCode(box_size=2, border=1)
qr.add_data(website)  # Or LinkedIn, contact card, etc.
qr.make(fit=True)
qr_img = qr.make_image(fill="black", back_color="white").convert("1")

# Paste QR code on the image (adjust position)
image.paste(qr_img, (width - 50, height - 50))  # Adjust for your layout

# Display the image on the e-Paper screen
epd.display(epd.getbuffer(image))
epd.sleep()  # Put the display to sleep to save power

print("Business card displayed successfully!")
