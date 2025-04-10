#! /bin/bash 

echo "Keystroke Logger by Team InnoSync"
echo "--------------------------------"

# Kill any existing keystroke logger processes
pkill -f "python3.*keylogger.py" 2>/dev/null

# Make the keylogger script executable
chmod +x "$(dirname "$0")/keylogger.sh"

echo "Starting keystroke logger..."
echo "The logger will capture each individual keystroke as you type."
echo "Press Ctrl+D to stop logging."

# Run the bash keystroke logger
"$(dirname "$0")/keylogger.sh"

echo "Keystroke logging session ended."
echo "Log file is saved at: $(dirname "$0")/keystroke_log.txt"

# Display the last few lines of the log file
echo ""
echo "Last recorded keystrokes:"
tail -n 10 "$(dirname "$0")/keystroke_log.txt"

read -p "Press Enter to exit" 
