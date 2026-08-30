import psutil
import time
import os


def clear_screen():
    os.system('clear')


def main():
    try:
        while True:
            clear_screen()
            processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']))

            print("=" * 70)
            print("GRAND LINE GUARDIAN - Live Ship (Process) Monitor")
            print("=" * 70)
            print(f"{'PID':<10}{'Name':<30}{'CPU %':<10}{'Memory %':<10}")
            print("-" * 70)

            sorted_procs = sorted(processes, key=lambda p: p.info['cpu_percent'] or 0, reverse=True)

            for proc in sorted_procs[:20]:
                pid = proc.info['pid']
                name = proc.info['name'] or "unknown"
                cpu = proc.info['cpu_percent'] or 0.0
                mem = proc.info['memory_percent'] or 0.0
                print(f"{pid:<10}{name[:28]:<30}{cpu:<10.1f}{mem:<10.2f}")

            print("-" * 70)
            print(f"Total Active Ships (Processes): {len(processes)}")
            print("\nPress Ctrl+C to stop monitoring.")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nGuardian shutting down. Fair winds, Captain.")


if __name__ == "__main__":
    main()
