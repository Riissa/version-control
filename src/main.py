from datetime import datetime

#This gets the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#This wWrite to the file version.md
with open("version.md", "w") as file:
    file.write(f"Last updated: {current_time}\n")

print("version.md updated :)!")
