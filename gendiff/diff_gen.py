#!/usr/bin/env python3
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_
from gendiff.interface import file_opener, mkfile, mk_sorted_file
import json
import yaml


def generate_diff(file1, file2, formater="stylish"):
    data1, format1 = file_opener(file1)
    data2, format2 = file_opener(file2)
    data1 = yaml.safe_load(data1) if format1 == "yaml" else json.load(data1)
    data2 = yaml.safe_load(data2) if format2 == "yaml" else json.load(data2)
    return format(data1, data2, formater)


def finder_logic(file1, file2):  # noqa C901
    answer = {}
    all_keys = set(file1).union(set(file2))

    for x in all_keys:
        if x in file1 and x in file2 and file1[x] == file2[x]:
            if not isinstance(file1[x], dict):
                info = mkfile(name=x, data=file1[x], status="same")
            else:
                info = mkfile(name=x, data=finder_logic(file1[x], file1[x]), status="same")  # noqa E501
        if x in file1 and x not in file2:
            if not isinstance(file1[x], dict):
                info = mkfile(name=x, data=file1[x], status="removed")
            else:
                info = mkfile(name=x, data=finder_logic(file1[x], file1[x]), status="removed")  # noqa E501
        if x in file2 and x not in file1:
            if not isinstance(file2[x], dict):
                info = mkfile(name=x, data=file2[x], status="added")
            else:
                info = mkfile(name=x, data=finder_logic(file2[x], file2[x]), status="added")  # noqa E501
        if x in file1 and x in file2 and file1[x] != file2[x]:
            if isinstance(file1[x], dict) and isinstance(file2[x], dict):
                info = mkfile(x, data=finder_logic(file1[x], file2[x]), status="nested")  # noqa E501
            else:
                old = finder_logic(file1[x], file1[x]) if isinstance(file1[x], dict) else file1[x]  # noqa E501
                new = finder_logic(file2[x], file2[x]) if isinstance(file2[x], dict) else file2[x]  # noqa E501
                info = mk_sorted_file(name=x, old_value=old, new_value=new)
        answer.update(info)
    return dict(sorted(answer.items(), key=lambda item: item[0]))


def format(file1, file2, needed_format):
    if needed_format == "stylish":
        return stylish(finder_logic(file1, file2))
    elif needed_format == "plain":
        return plain(finder_logic(file1, file2))
    elif needed_format == "json":
        return json_(finder_logic(file1, file2))
    return "unsupported format!"
