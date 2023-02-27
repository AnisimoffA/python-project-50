import json
from gendiff.interface import none_to_null


def to_json(item):
    item = none_to_null(item)
    return json.dumps(item, indent=4)
