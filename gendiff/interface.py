#!/usr/bin/env python3
import yaml
import json


def filt(z):
    if z == None: # noqa
        return "null"
    if isinstance(z, bool):
        return str(z).lower()
    else:
        return z


def file_opener(file):
    file_form = file.split(".")[1]
    if "/" in file:
        if "jaml" in file:
            return yaml.safe_load(open(file))
        elif "jml" in file:
            return yaml.safe_load(open(file.replace("jml", "jaml")))
        return yaml.safe_load(open(file))

    if file_form == "jaml" or file_form == "jml":
        return yaml.safe_load(open(f"tests/fixtures/{file.split('.')[0]}.{'jaml'}"))  # noqa
    return json.load(open(f"tests/fixtures/{file}"))


def local_formater(item, format):
    if not isinstance(item, dict):
        if item == "false" or item == "true" or item == "null":
            return item
        if isinstance(item, int):
            return item
        return f"\'{item}\'" if format == "plain" else f"\"{item}\""
    return "[complex value]"


def mkfile(name, data=[], status=''):
    return {name: {'changes': data, 'status': status}}


def mk_sorted_file(name, status='changed', old_value={}, new_value={}):
    return {name: {'status': status, "old_value": old_value, "new_value": new_value}}  # noqa
