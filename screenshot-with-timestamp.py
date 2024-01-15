from PIL import ImageGrab, ImageDraw, ImageFont
import datetime

def screenshot_with_timestamp():
    # Get the current time
    now = datetime.datetime.now()

    # Take a screenshot of all monitors
    screenshot = ImageGrab.grab()

    # Format the timestamp string to show time up to minutes
    timestamp_str = now.strftime("%d-%m-%y %H:%M")

    # Add a timestamp to the screenshot
    draw = ImageDraw.Draw(screenshot)
    font = ImageFont.truetype("arial.ttf", 22)
    position = (10, 10)

    # Draw a background for the text with some margins
    left, top, right, bottom = draw.textbbox(position, timestamp_str, font=font)
    draw.rectangle((left-5, top-5, right+5, bottom+5), fill="blue")

    # Draw a timestamp
    draw.text(position, timestamp_str, font=font, fill="white")

    # Save the screenshot to a file
    screenshot.save("screenshot.png")

screenshot_with_timestamp()
