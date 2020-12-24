import json
from pathlib import Path

def write_json(dictionary): 
    json_object = json.dumps(dictionary)
    data_folder = Path("src/config/output.json")
    with open(data_folder, "w") as outfile: 
        outfile.write(json_object) 
