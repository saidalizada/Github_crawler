import json
from pathlib import Path

def load_json(filepath):
    data_folder = Path(filepath)
    with open(data_folder, encoding="utf8") as f:
        data = json.load(f)
    return data
