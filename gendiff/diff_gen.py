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


def to_find_diff(file1, file2):

    answer = []
    for item in sorted(set(file1).union(set(file2))):
        if item in file1 and item not in file2:
            info = {"key": item, "status": "removed", "changes": file1[item]}
        elif item in file2 and item not in file1:
            info = {"key": item, "status": "added", "changes": file2[item]}
        elif isinstance(file1[item], dict) and isinstance(file2[item], dict):
            info = {"key": item, "status": "nested", "changes": to_find_diff(file1[item], file2[item])}  # noqa E501
        elif file1[item] == file2[item]:
            info = {"key": item, "status": "same", "changes": file1[item]}
        else:
            info = {'key': item, 'status': "changed", "old_value": file1[item], "new_value": file2[item]}  # noqa E501
        answer.append(info)
    return answer


def format(file1, file2, needed_format):
    if needed_format == "stylish":
        return to_stylish(to_find_diff(file1, file2))
    elif needed_format == "plain":
        return to_plain(to_find_diff(file1, file2))
    elif needed_format == "json":
        return to_json(to_find_diff(file1, file2))
    return "unsupported format!"
