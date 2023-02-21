#!/usr/bin/env python3
from pathlib import Path
import yaml
import json


def filt(z):
    if z is None:
        return "null"
    if isinstance(z, bool):
        return str(z).lower()
    else:
        return z


def none_to_null(item):
    for k, v in item.items():
        if isinstance(v, dict):
            none_to_null(v)
        else:
            item[k] = filt(v)
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


def parser(data, format):
    return yaml.safe_load(data) if format == "yaml" else json.load(data)
