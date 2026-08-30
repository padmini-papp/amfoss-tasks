Operation Pixel Merge

There were 86 images in the assets folder, each 512x512, with a single colored dot on a white background, except for a few that were completely blank white. The files were named like Layer 1.png, Layer 2.png and so on, but sorting them the normal way puts them in the wrong order since it goes alphabetically instead of numerically, so I had to pull the number out of each filename with a regex and sort by that instead.

For every image I used OpenCV to find the dot. I converted the image to grayscale, thresholded it so anything that wasn't close to white got picked out, then averaged the coordinates of those picked out pixels to find the center of the dot. I also grabbed the actual pixel color at that spot so I knew what color to draw the connecting line in. If an image had no dot at all, meaning it was pure white, that counted as a break, so no line got drawn into or out of that image.

Using Pillow, I drew a line from each dot to the next one in the sequence, using the color of the starting dot, all on one blank canvas. Running the script produces output.png, which turned out to be a picture of a lightbulb.

How to run

pip install opencv-python pillow
python3 merge.py

Files

merge.py is the script, output.png is the result.
