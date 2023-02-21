#!/usr/bin/env python3
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_
from gendiff.interface import file_opener, parser, none_to_null


def generate_diff(file1, file2, formater="stylish"):
    data1, format1 = file_opener(file1)
    data2, format2 = file_opener(file2)
    data1 = none_to_null(parser(data1, format1))
    data2 = none_to_null(parser(data2, format2))
    return format(data1, data2, formater)


def finder_logic(file1, file2):  # noqa C901

    answer = []
    for x in set(file1).union(set(file2)):
        if x in file1 and x in file2 and file1[x] == file2[x]:
            info = {"key": x, "changes": file1[x], "status": "same"}
        if x in file1 and x not in file2:
            info = {"key": x, "changes": file1[x], "status": "removed"}
        if x in file2 and x not in file1:
            info = {"key": x, "changes": file2[x], "status": "added"}
        if x in file1 and x in file2 and file1[x] != file2[x]:
            if isinstance(file1[x], dict) and isinstance(file2[x], dict):
                info = {"key": x, "changes": finder_logic(file1[x], file2[x]), "status": "nested"}  # noqa E501
            else:
                info = {'key': x, 'status': "changed", "old_value": file1[x], "new_value": file2[x]}  # noqa E501
        answer.append(info)
    return sorted(answer, key=lambda item: item["key"])


def format(file1, file2, needed_format):
    if needed_format == "stylish":
        return stylish(finder_logic(file1, file2))
    elif needed_format == "plain":
        return plain(finder_logic(file1, file2))
    elif needed_format == "json":
        return json_(finder_logic(file1, file2))
    return "unsupported format!"
