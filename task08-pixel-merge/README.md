# Operation Pixel Merge

Task 08 for amFOSS. There were 86 images in the assets folder, each 512x512, with a single colored dot on a white background (or completely blank white for a few of them). The filenames were like "Layer 1.png", "Layer 2.png" etc but just sorting them normally with ls or os.listdir puts them in the wrong order (Layer 1, Layer 10, Layer 11... instead of 1, 2, 3), so I had to extract the number from each filename with a regex and sort numerically.

For each image I used OpenCV to find where the dot is - converted to grayscale, thresholded so anything not close to white becomes highlighted, then found the average position of all the highlighted pixels to get the dot's center coordinate. I also sampled the actual pixel color at that point so I know what color line to draw.

If an image had no dot at all (completely white), I treat that as a break, meaning I don't draw a line into or out of it.

Then using Pillow, I drew a line from each dot to the next one in sequence, colored using the starting dot's color, on a blank white canvas.

Running it produces output.png, which shows a lightbulb picture.

## How to run

pip install opencv-python pillow
python3 merge.py

## Files

merge.py - the actual script
output.png - the final result
