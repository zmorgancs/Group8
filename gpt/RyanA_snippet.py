import datetime

# Logs a INFO, WARNING, and ERROR message
def log_message(level, message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{level}] {current_time}: {message}")

# Output message
log_message("INFO", "This is an informational message.")
log_message("WARNING", "This is a warning message.")
log_message("ERROR", "This is an error message.")
