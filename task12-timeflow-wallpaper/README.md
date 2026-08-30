# TimeFlow Wallpaper Sync

Task 12 for amFOSS. A Python script that watches a text file and displays its content directly on the desktop wallpaper, along with a live updating clock.

## Approach

The script generates a new image using Pillow every second. It draws:
1. The current time (updating every second) and date at the top
2. The contents of a user-provided text file below that

It then uses macOS's AppleScript (via the osascript command, run through Python's subprocess module) to set this generated image as the desktop wallpaper.

The main loop checks two things every second:
1. Has the text file's last-modified timestamp changed? (meaning the user edited it)
2. Has the clock's second value changed? (to keep the time live)

If either is true, it regenerates the image and reapplies it as the wallpaper. This means the wallpaper updates automatically both when you edit your notes file, and continuously to keep the clock accurate.

## Challenges faced

Getting macOS to actually accept the new wallpaper wasn't obvious at first, since nothing happened on the first try. Had to check System Settings > Privacy & Security > Automation to make sure Terminal had permission to control System Events before the AppleScript command would actually work.

## How to run

pip install pillow
python3 wallpaper_sync.py <path_to_text_file>

Example:
python3 wallpaper_sync.py my_notes.txt

Press Ctrl+C to stop watching.

## Concepts learned

- Using Pillow (PIL) to generate images with text drawn on them, including using custom fonts
- Using Python's subprocess module to call an AppleScript command (osascript) from Python, to interact with macOS system settings
- Watching a file for changes using os.path.getmtime() instead of a dedicated file-watching library
- macOS automation permissions and how they can silently block scripts from controlling system settings until explicitly granted
