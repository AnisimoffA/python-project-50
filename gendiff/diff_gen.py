#!/usr/bin/env python3
import json
from gendiff import interface


def generate_diff(file1, file2): # noqa
    file1 = json.load(open(f"tests/fixtures/{file1}"))
    file2 = json.load(open(f"tests/fixtures/{file2}"))

    def inside_func(file1, file2):
        same_items = []
        for x in set(file1) & set(file2):
            if file1[x] == file2[x]:
                if not isinstance(file1[x], dict):
                    same_items.append(["", x, file1[x]])
                else:
                    same_items.append(["", x, inside_func(file1[x], file1[x])])

        only_in_1st = []
        for x in set(file1) - set(file2):
            if not isinstance(file1[x], dict):
                only_in_1st.append(["-", x, file1[x]])
            else:
                only_in_1st.append(["-", x, inside_func(file1[x], file1[x])])

        only_in_2nd = []
        for x in set(file2) - set(file1):
            if not isinstance(file2[x], dict):
                only_in_2nd.append(["+", x, file2[x]])
            else:
                only_in_2nd.append(["+", x, inside_func(file2[x], file2[x])])

        union_items = same_items + only_in_1st + only_in_2nd
        only_names = (set(list(map(lambda x: x[1], union_items))))

        same_keys_diff_vals = set(file1).union(set(file2)) - only_names

        for x in same_keys_diff_vals:
            if not isinstance(file1[x], dict) or not isinstance(file2[x], dict):
                union_items.append(["-", x, file1[x]]) if not isinstance(file1[x], dict) else union_items.append(["-", x, inside_func(file1[x], file1[x])])  # noqa: E501
                union_items.append(["+", x, file2[x]]) if not isinstance(file2[x], dict) else union_items.append(["+", x, inside_func(file1[x], file1[x])])  # noqa: E501

            else:
                union_items.append(["", x, inside_func(file1[x], file2[x])])

        sort_list = interface.sort_items(union_items)

        return sort_list
    return inside_func(file1, file2)
