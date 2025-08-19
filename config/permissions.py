import json

PERMISSIONS_PATH = "config/permissions.json"

def load_permissions():
    with open(PERMISSIONS_PATH, "r") as f:
        return json.load(f)

def is_allowed(module):
    permissions = load_permissions()
    return permissions.get(module, False)