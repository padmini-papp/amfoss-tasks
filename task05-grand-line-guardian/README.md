## Grand Line Guardian

This is a terminal based system monitor, similar to htop, that shows live info about running processes on the machine.

I used a Python library called psutil, which reads process information straight from the operating system, so there was no need to write any low level system calls myself.

The program loops continuously: it grabs a fresh list of every running process using psutil.process_iter(), sorts them by CPU usage so the busiest ones show up first, clears the terminal and reprints a table with PID, process name, CPU percent, and memory percent, along with the total number of active processes. It refreshes every second and can be stopped cleanly with Ctrl+C.

<b>
### **Concepts learned**
Reading OS level process info through psutil instead of raw system calls, getting a live snapshot of processes with process_iter, refreshing a terminal display by clearing and reprinting instead of using a proper UI library, and handling a KeyboardInterrupt so the program exits cleanly instead of throwing an error when the user presses Ctrl+C.
<br>

### **How to run**

pip install psutil
python3 guardian.py

Prss Ctrl+C to stop.
