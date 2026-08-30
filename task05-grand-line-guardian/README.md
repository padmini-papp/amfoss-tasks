# Grand Line Guardian

Task 05 for amFOSS. A terminal based system process monitor, similar to htop/btop, themed around tracking "ships" (processes) sailing the Grand Line.

## Approach

Used Python's psutil library, which handles reading process information (PID, name, CPU usage, memory usage) from the operating system directly, so I didn't have to write low level system calls myself.

The program runs in a loop:
1. Get a fresh snapshot of all running processes using psutil.process_iter()
2. Sort them by CPU usage, highest first, so the busiest processes show at the top
3. Clear the terminal screen and print a formatted table of the top 20 processes
4. Show the total count of all active processes
5. Wait 1 second, then repeat

Ctrl+C stops the monitor cleanly with a shutdown message instead of an ugly error trace.

## Displayed info

- Process ID (PID)
- Process Name
- CPU %
- Memory %
- Total active process count

## Concepts learned

- psutil library for reading OS-level process information in Python without writing raw system calls
- process_iter() for getting a live snapshot of all running processes
- Basic terminal UI refresh technique (clearing the screen and reprinting) to simulate a live updating dashboard
- Handling KeyboardInterrupt (Ctrl+C) to exit a loop cleanly instead of crashing

## How to run

pip install psutil
python3 guardian.py

Press Ctrl+C to stop.
