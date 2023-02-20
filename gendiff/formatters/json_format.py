import json
from gendiff.interface import none_to_null_filt


def json_(item):
    item = none_to_null_filt(item)
    return json.dumps(item, indent=4)
