import json

FILE = "database/memory.json"

def load_memory():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(key, value):
    data = load_memory()
    data[key] = value
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
