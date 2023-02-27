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
    for item in sorted(set(file1).union(set(file2))):
        if item in file1 and item not in file2:
            info = {"key": item, "changes": file1[item], "status": "removed"}
        elif item in file2 and item not in file1:
            info = {"key": item, "changes": file2[item], "status": "added"}
        elif file1[item] != file2[item]:
            if isinstance(file1[item], dict) and isinstance(file2[item], dict):
                info = {"key": item, "changes": finder_logic(file1[item], file2[item]), "status": "nested"}  # noqa E501
            else:
                info = {'key': item, 'status': "changed", "old_value": file1[item], "new_value": file2[item]}  # noqa E501
        else:
            info = {"key": item, "changes": file1[item], "status": "same"}
        answer.append(info)
    return answer


def format(file1, file2, needed_format):
    if needed_format == "stylish":

        return to_stylish(finder_logic(file1, file2))
    elif needed_format == "plain":

        return to_plain(finder_logic(file1, file2))
    elif needed_format == "json":

        return to_json(finder_logic(file1, file2))
    return "unsupported format!"

