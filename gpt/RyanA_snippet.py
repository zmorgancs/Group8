import datetime

def log_info(message):
    current_time = datetime.datetime.now()
    print(f"[INFO] {current_time}: {message}")

def log_warning(message):
    current_time = datetime.datetime.now()
    print(f"[WARNING] {current_time}: {message}")

def log_error(message):
    current_time = datetime.datetime.now()
    print(f"[ERROR] {current_time}: {message}")

log_info("This is an informational message.")
log_warning("This is a warning message.")
log_error("This is an error message.")
