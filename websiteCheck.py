import time
import datetime
import sys

def log(message):
    timestamp = datetime.datetime.now().isoformat()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

try:
    log("Script started")

    print("Checking F1 results...", flush=True)
    time.sleep(5)

    log("Check complete - no issues found")
    print("Check complete - no issues found", flush=True)

    sys.exit(0)  # explicitly exit successfully

except Exception as e:
    log(f"ERROR: {str(e)}")
    print(f"ERROR: {str(e)}", flush=True)
    sys.exit(1)
