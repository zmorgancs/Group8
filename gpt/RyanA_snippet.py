import datetime

def log_message(level, message):
    current_time = datetime.datetime.now()
    print(f"[{level}] {current_time}: {message}")

log_message("INFO", "This is an informational message.")
log_message("WARNING", "This is a warning message.")
log_message("ERROR", "This is an error message.")
