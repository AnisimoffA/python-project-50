#!/usr/bin/env python3
from pathlib import Path
import yaml
import json


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


def parser(data, format):
    if format == "yaml":
        return yaml.safe_load(data)
    elif format == "json":
        return json.load(data)
    return "incorrect format"
