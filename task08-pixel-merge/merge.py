import cv2
import numpy as np
from PIL import Image, ImageDraw
import os
import re

ASSETS_DIR = "assets"

files = os.listdir(ASSETS_DIR)

def get_num(filename):
    match = re.search(r'\d+', filename)
    return int(match.group())

files.sort(key=get_num)

points = []

for f in files:
    path = os.path.join(ASSETS_DIR, f)
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    coords = cv2.findNonZero(mask)

    if coords is None:
        points.append(None)
        continue

    coords = coords.reshape(-1, 2)
    x = int(np.mean(coords[:, 0]))
    y = int(np.mean(coords[:, 1]))

    b, g, r = img[y, x]
    color = (int(r), int(g), int(b))

    points.append((x, y, color))

canvas = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(canvas)

for i in range(len(points) - 1):
    current = points[i]
    nxt = points[i + 1]

    if current is None or nxt is None:
        continue

    x1, y1, color = current
    x2, y2, _ = nxt

    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)

canvas.save("output.png")
print("Done! Saved as output.png")
