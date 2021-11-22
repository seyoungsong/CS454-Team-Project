import json
import os


DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../seyoung/data.json"
TOTAL_COVERAGE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/total_coverage.json'

def read_json(path=DATA_PATH):
    js_object = None
    with open(path, "r") as data:
        js_object = json.loads(data.read())
    return js_object

# print(read_json())