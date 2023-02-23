#!/usr/bin/env python3
from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json
from gendiff.interface import file_opener, parser


def generate_diff(file1, file2, formater="stylish"):
    data1, format1 = file_opener(file1)
    data2, format2 = file_opener(file2)
    data1 = parser(data1, format1)
    data2 = parser(data2, format2)
    return format(data1, data2, formater)


def finder_logic(file1, file2):

    answer = []
    for x in sorted(set(file1).union(set(file2))):
        if x in file1 and x not in file2:
            info = {"key": x, "changes": file1[x], "status": "removed"}
        elif x in file2 and x not in file1:
            info = {"key": x, "changes": file2[x], "status": "added"}
        else:
            if file1[x] != file2[x]:
                if isinstance(file1[x], dict) and isinstance(file2[x], dict):
                    info = {"key": x, "changes": finder_logic(file1[x], file2[x]), "status": "nested"}  # noqa E501
                else:
                    info = {'key': x, 'status': "changed", "old_value": file1[x], "new_value": file2[x]}  # noqa E501
            else:
                info = {"key": x, "changes": file1[x], "status": "same"}
        answer.append(info)
    return answer


def format(file1, file2, needed_format):
    if needed_format == "stylish":
        file1 = none_to_null(file1)
        file2 = none_to_null(file2)
        return to_stylish(finder_logic(file1, file2))
    elif needed_format == "plain":
        file1 = none_to_null(file1)
        file2 = none_to_null(file2)
        return to_plain(finder_logic(file1, file2))
    elif needed_format == "json":
        file1 = none_to_null(file1)
        file2 = none_to_null(file2)
        return to_json(finder_logic(file1, file2))
    return "unsupported format!"


def filt(item):
    if item is None:
        return "null"
    if isinstance(item, bool):
        return str(item).lower()
    else:
        return item


def none_to_null(item):
    for key, value in item.items():
        if isinstance(value, dict):
            none_to_null(value)
        else:
            item[key] = filt(value)
    return item
