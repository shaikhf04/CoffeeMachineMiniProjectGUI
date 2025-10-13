import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a new log file per session, based on current timestamp
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
log_file = os.path.join(LOG_DIR, log_filename)

# Create (overwrite) the log file at startup
with open(log_file, "w") as f:
    f.write(f"=== New Coffee Bot Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

# Logger function (appends to this session's file)
def logger(msg, mytype="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{mytype}] - {msg}"
    
    # Optional: print to console
    # print(log_line)

    with open(log_file, "a") as f:
        f.write(log_line + "\n")
