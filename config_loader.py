import json
from logger import log

_config = None
def load_config():
    log("Loading config...")
    global _config
    if _config is None:
        try:
            print("Loading Config.....")
            with open ("config.json", "r") as file:
                _config = json.load(file)
        except FileNotFoundError:
            log("config.json not found", "ERROR")
            print("X config.json file not found")
            return None
        except json.JSONDecodeError:
            print("X Invalid JSON format")
            _config = {}
    return _config

def reload_config():
    global _config
    _config = None
    return load_config()