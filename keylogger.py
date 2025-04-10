#!/usr/bin/env python3
import time
from datetime import datetime
import os
import sys

# Configuration
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keystroke_log.txt")

def log_input(text):
    """Log input text to file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} - Input: {text}\n")
        # Force write to disk
        log_file.flush()
        os.fsync(log_file.fileno())

def main():
    """Main function to start the logger"""
    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(f"Keystroke Logging Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 50 + "\n")
    else:
        with open(LOG_FILE, "a") as f:
            f.write(f"\nNew Logging Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 50 + "\n")
    
    print("Keystroke Logger by Team InnoSync")
    print("-" * 30)
    print("\nLogging keystrokes in real-time.")
    print("Type anything below (each character will be logged immediately):")
    print("Press Ctrl+C to exit.")
    
    try:
        # Buffer to collect characters
        buffer = ""
        
        while True:
            # Get a character from input
            char = input("")
            
            # Log the character
            log_input(char)
            
            # Print confirmation
            print(f"Logged: {char}")
            
    except KeyboardInterrupt:
        print("\nKeylogging stopped by user.")
    
    # Log session end
    with open(LOG_FILE, "a") as f:
        f.write(f"\nLogging Session Ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
    
    print(f"Keystroke logging stopped. Log saved to: {LOG_FILE}")

if __name__ == "__main__":
    main()
