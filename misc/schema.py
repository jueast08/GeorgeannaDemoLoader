import json
import os

def validationSchema():
    pwd = os.path.dirname(os.path.realpath(__file__))
    with open(pwd+"/schema.json") as f:
        return json.load(f)
