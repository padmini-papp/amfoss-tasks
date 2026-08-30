from PIL import Image, ImageDraw, ImageFont
import os
import time
import subprocess
import sys
from datetime import datetime


def get_screen_size():
    return (1920, 1080)


def generate_wallpaper(text_content, output_path):
    width, height = get_screen_size()
    img = Image.new("RGB", (width, height), color=(20, 20, 30))
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 60)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%A, %B %d, %Y")

    draw.text((width // 2, 100), time_str, font=font_large, fill=(255, 255, 255), anchor="mm")
    draw.text((width // 2, 170), date_str, font=font_small, fill=(180, 180, 180), anchor="mm")

    lines = text_content.split("\n")
    y = 280
    for line in lines:
        draw.text((80, y), line, font=font_small, fill=(220, 220, 220))
        y += 40

    img.save(output_path)


def set_wallpaper_mac(image_path):
    script = f'''
    tell application "System Events"
        tell every desktop
            set picture to "{image_path}"
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script])


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 wallpaper_sync.py <path_to_text_file>")
        return

    text_file = sys.argv[1]
    output_path = os.path.abspath("wallpaper_output.png")

    last_modified = None
    last_second = None

    print(f"Watching {text_file} for changes. Press Ctrl+C to stop.")

    try:
        while True:
            current_modified = os.path.getmtime(text_file) if os.path.exists(text_file) else None
            current_second = datetime.now().second

            if current_modified != last_modified or current_second != last_second:
                if os.path.exists(text_file):
                    with open(text_file, "r") as f:
                        content = f.read()
                else:
                    content = "(file not found)"

                generate_wallpaper(content, output_path)
                set_wallpaper_mac(output_path)

                last_modified = current_modified
                last_second = current_second

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped watching.")


if __name__ == "__main__":
    main()
