import json

def load_json(filepath):
    with open(filepath, encoding="utf8") as f:
        data = json.load(f)
    return data