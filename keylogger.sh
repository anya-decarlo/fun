#!/bin/bash

# Configuration
LOG_FILE="$(dirname "$0")/keystroke_log.txt"

# Create log file if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
  echo "Keystroke Logging Started: $(date '+%Y-%m-%d %H:%M:%S')" > "$LOG_FILE"
  echo "--------------------------------------------------" >> "$LOG_FILE"
else
  echo "" >> "$LOG_FILE"
  echo "New Logging Session: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
  echo "--------------------------------------------------" >> "$LOG_FILE"
fi

# Display instructions
echo "Keystroke Logger by Team InnoSync"
echo "--------------------------------"
echo ""
echo "Recording keystrokes. Press Ctrl+D to exit."
echo "Type anything below:"
echo ""

# Read characters one by one and log them
while IFS= read -r -n1 char; do
  if [ -n "$char" ]; then
    timestamp=$(date '+%Y-%m-%d %H:%M:%S.%3N')
    echo "$timestamp - Key: $char" >> "$LOG_FILE"
    # Immediately flush to disk
    sync
  fi
done

# Log session end
echo "" >> "$LOG_FILE"
echo "Logging Session Ended: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
echo "--------------------------------------------------" >> "$LOG_FILE"

echo ""
echo "Keystroke logging stopped."
echo "Log file is saved at: $LOG_FILE"
