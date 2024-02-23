import datetime  # Importing the datetime module to work with dates and times

def log_message(level, message):
    # Retrieve the current time and format it as a string in "YYYY-MM-DD HH:MM:SS" format
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Print the log message including the level, current time, and the message content
    print(f"[{level}] {current_time}: {message}")

# Printing log messages with different severity levels using the log_message function
log_message("INFO", "This is an informational message.")  # INFO level message
log_message("WARNING", "This is a warning message.")      # WARNING level message
log_message("ERROR", "This is an error message.")         # ERROR level message
