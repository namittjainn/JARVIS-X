from core.memory import save_memory, load_memory
from data.knowledge import search_web
from system.control import system_action

def process_command(command):
    memory = load_memory()

    if "my name is" in command:
        name = command.replace("my name is", "").strip()
        save_memory("name", name)
        return f"I will remember your name, {name}"

    if "what is my name" in command:
        return f"Your name is {memory.get('name', 'not stored yet')}"

    if "open" in command or "shutdown" in command:
        system_action(command)
        return "System command executed"

    return search_web(command)
