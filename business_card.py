#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("business card demo")

    # Initialize the e-Paper display
    epd = epd2in13_V4.EPD()
    epd.init()
    epd.Clear(0xFF)

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    if 1: 
        epd.init()
        image = Image.new('1', (epd.height, epd.width, 255)
        draw = ImageDraw.Draw(image)      

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

    else:
        epd.init_fast()
        image = Image.new('1', (epd.height, epd.width, 255)
        draw = ImageDraw.Draw(image)      

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
