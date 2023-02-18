#!/usr/bin/env python3
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_ as json
from gendiff.interface import file_opener, filt, mkfile, mk_sorted_file


def generate_diff(file1, file2, formater="stylish"):
    file1 = file_opener(file1)
    file2 = file_opener(file2)

    def inside_func(file1, file2):
        return finder_logic(file1, file2)

    if formater == "stylish":
        return stylish(inside_func(file1, file2))
    elif formater == "plain":
        return plain(inside_func(file1, file2))
    return json(inside_func(file1, file2))


def finder_logic(file1, file2):
    folder = {}
    folder.update(seacher(file1, file2, "same_file"))
    folder.update(seacher(file1, file2, "only1_file"))
    folder.update(seacher(file1, file2, "only2_file"))

    folder_names = set(list(map(lambda x: x, folder)))
    same_keys_diff_vals = set(file1).union(set(file2)) - folder_names

    for x in same_keys_diff_vals:
        if isinstance(file1[x], dict) and isinstance(file2[x], dict):
            union_dict = mkfile(x, data=finder_logic(file1[x], file2[x]), status="nested")  # noqa
        else:
            old = finder_logic(file1[x], file1[x]) if isinstance(file1[x], dict) else filt(file1[x])  # noqa
            new = finder_logic(file2[x], file2[x]) if isinstance(file2[x], dict) else filt(file2[x])  # noqa
            union_dict = mk_sorted_file(name=x, old_value=old, new_value=new)

        folder.update(union_dict)
    return dict(sorted(folder.items(), key=lambda item: item[0]))


def seacher(file1, file2, condition):  # noqa
    answer = {}

    if condition == "same_file":
        items = list(filter(lambda x: file1[x] == file2[x], set(file1) & set(file2)))  # noqa
        status = "same"
    elif condition == "only1_file":
        items = set(file1) - set(file2)
        status = "removed"
    elif condition == "only2_file":
        items = set(file2) - set(file1)
        status = "added"

    for x in items:
        if condition == "only2_file":
            if not isinstance(file2[x], dict):
                info = mkfile(name=x, data=filt(file2[x]), status=status)
            else:
                info = mkfile(name=x, data=finder_logic(file2[x], file2[x]), status=status)  # noqa
            answer.update(info)
        else:
            if not isinstance(file1[x], dict):
                info = mkfile(name=x, data=filt(file1[x]), status=status)
            else:
                info = mkfile(name=x, data=finder_logic(file1[x], file1[x]), status=status)  # noqa
            answer.update(info)

    return answer

print(generate_diff("nonflatten_before.json", "nonflatten_after.json", "stylish"))