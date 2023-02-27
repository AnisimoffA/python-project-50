#!/usr/bin/env python3
from pathlib import Path
import yaml
import json

#--------------old version----------------

# def file_opener(file):
#     file_format = file.split(".")[1]

#     if file_format == 'json':
#         if "/" in file:
#             data = open(file)
#         else:
#             data = open(f"tests/fixtures/{file}")
#     elif file_format == 'yml' or file_format == 'yaml':
#         if "/" in file:
#             data = Path(file).read_text()
#         else:
#             data = Path(f"tests/fixtures/{file.split('.')[0]}.{'yaml'}").read_text()  # noqa E501
#         file_format = "yaml"
#     return data, file_format

#--------------new version----------------
def file_opener(file):
    file_format = file.split(".")[1]

    if file_format == 'json':
        data = open(file)
    elif file_format == 'yml' or file_format == 'yaml':
        data = Path(file).read_text()
    return data, file_format


def parser(data, format):
    if format == "yaml":
        return yaml.safe_load(data)
    elif format == "json":
        return json.load(data)
    return "incorrect format"


def none_to_null(item):
    if item is None:
        return "null"
    elif isinstance(item, bool):
        return str(item).lower()
    elif isinstance(item, dict):
        for _, v in item.items():
            none_to_null(v)
    elif isinstance(item, list):
    
        for x in item:
            if x["status"] == "changed":
                x["old_value"] = none_to_null(x["old_value"])
                x["new_value"] = none_to_null(x["new_value"])
            elif isinstance(x["changes"], list):
                none_to_null(x["changes"])
            else:
                x["changes"] = none_to_null(x["changes"])
        return item
    return item
