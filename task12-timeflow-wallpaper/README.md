## TimeFlow Wallpaper Sync

This is a script that watches a text file and displays its content directly on the desktop wallpaper, along with a live clock.

I used Pillow to generate a new image every second, drawing the current time and date at the top, and whatever text is inside the given file below that. To actually apply it as the desktop wallpaper, I used osascript through Python's subprocess module, which lets you run AppleScript commands, the scripting language macOS uses to control system settings like the wallpaper.

The main loop checks two things every second, whether the text file's last modified time has changed, meaning the user edited it, and whether the clock's second value has ticked over. If either changed, it regenerates the image and reapplies it as the wallpaper.

### Issues faced

The first time I ran it, nothing happened on my actual desktop, even though the generated image looked correct when I opened it separately in Preview. It turned out macOS was silently blocking the script from changing the wallpaper because Terminal didn't have permission. I had to go into System Settings, Privacy and Security, Automation, and allow Terminal to control System Events before it worked properly.

### How to run

pip install pillow
python3 wallpaper_sync.py my_notes.txt

Press Ctrl+C to stop watching.
