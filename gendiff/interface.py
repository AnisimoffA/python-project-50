#!/usr/bin/env python3
from pathlib import Path
import yaml
import json


def file_opener(file):
    file_name = file.split(".")[0]
    file_format = file.split(".")[1]

    if file_format == 'json':
        data = open(file)
    elif file_format == 'yaml' or file_format == 'yml':
        file_format = 'yaml'
        data = Path(file).read_text()
    return data, file_format


def parser(data, format):
    if format == "yaml":
        return yaml.safe_load(data)
    elif format == "json":
        return json.load(data)
    return "incorrect format"


def none_to_null(item): # noqa C901
    if item is None:
        return "null"
    elif isinstance(item, bool):
        return str(item).lower()
    elif isinstance(item, dict):
        for v in item.values():
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
