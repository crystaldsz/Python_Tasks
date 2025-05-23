# Simple Log Writer
# Write logs to a file every time the script is run with timestamps.

from datetime import datetime
time_now = datetime.now()
message = "Script ran at: " + str(time_now) + "\n"
file = open("log.txt", "a")
file.write(message)
file.close()
print("Log saved.")