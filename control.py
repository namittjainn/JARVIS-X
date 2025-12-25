import os

def system_action(command):
    if "notepad" in command:
        os.system("notepad")
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
