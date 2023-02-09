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

    if file_form == "jaml" or file_form == "jml":
        return yaml.safe_load(open(f"tests/fixtures/{file.split('.')[0]}.{'jaml'}"))  # noqa
    else:
        return json.load(open(f"tests/fixtures/{file}"))


def to_sorted_dict(items):
    items = sorted(items, key=lambda x: x[1])

    return {f"{mark} {k}" if mark != "" else k:
            filt(v) if not isinstance(v, list) else to_sorted_dict(v)
            for mark, k, v in items}


def to_sorted_list(items):
    items = sorted(items, key=lambda x: x[1])
    return [[mark, k, filt(v)] if not isinstance(v, list)
            else [mark, k, to_sorted_list(v)] for mark, k, v in items]


def find_changed_values(items):
    needed_items = list(filter(lambda x: "change" in x[0], items))
    other_items = list(filter(lambda x: "change" not in x[0], items))

    if not needed_items:
        return items

    correct_marks = list(map(lambda x: [x[0][6:], x[1], x[2]], needed_items))
    good_format = []

    for old, new in zip(*[iter(correct_marks)] * 2):
        good_format.append(["changed", old[1], {"old": old[2], "new": new[2]}])

    answer = to_sorted_list(other_items + good_format)
    return answer


def local_formater(item):
    if not isinstance(item, list):
        if item == "false" or item == "true" or item == "null":
            return item
        return f"\'{item}\'"
    return "[complex value]"
