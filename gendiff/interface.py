#!/usr/bin/env python3
from pathlib import Path


def filt(z):
    if z is None:
        return "null"
    if isinstance(z, bool):
        return str(z).lower()
    else:
        return z


def none_to_null_filt(item):
    for v in item.values():
        if v["status"] == "changed":
            if isinstance(v["old_value"], dict):
                none_to_null_filt(v["old_value"])
            else:
                v["old_value"] = filt(v["old_value"])
            if isinstance(v["new_value"], dict):
                none_to_null_filt(v["new_value"])
            else:
                v["new_value"] = filt(v["new_value"])
        else:
            if isinstance(v["changes"], dict):
                none_to_null_filt(v["changes"])
            v["changes"] = filt(v["changes"])
    return item


def file_opener(file):
    file_format = file.split(".")[1]

    if file_format == 'json':
        if "/" in file:
            data = open(file)
        else:
            data = open(f"tests/fixtures/{file}")
    elif file_format == 'yml' or file_format == 'yaml':
        if "/" in file:
            data = Path(file).read_text()
        else:
            data = Path(f"tests/fixtures/{file.split('.')[0]}.{'yaml'}").read_text()  # noqa E501
        file_format = "yaml"
    return data, file_format


def local_formater(item, format):
    if not isinstance(item, dict):
        if item == "false" or item == "true" or item == "null":
            return item
        if isinstance(item, int):
            return item
        return f"\'{item}\'" if format == "plain" else f"\"{item}\""
    return "[complex value]"


def mkfile(name, data=[], status=''):
    return {name: {'key': name, 'changes': data, 'status': status}}


def mk_sorted_file(name, status='changed', old_value={}, new_value={}):
    return {name: {'key': name, 'status': status, "old_value": old_value, "new_value": new_value}}  # noqa E501
