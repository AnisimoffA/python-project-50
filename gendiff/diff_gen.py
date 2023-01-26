#!/usr/bin/env python3
import json


def generate_diff(file1, file2):
    file1 = json.load(open(f"tests/fixtures/{file1}"))
    file2 = json.load(open(f"tests/fixtures/{file2}"))

    difference_list = []

    for k, v in file1.items():
        if k in file2.keys() and v in file2.values():
            file2.pop(k)
            difference_list.append(["   ", k + ":", v])
            continue

        if k not in file2.keys():
            difference_list.append(["  -", k + ":", v])
            continue

        if k in file2.keys() and v not in file2.values():
            difference_list.append(["  -", k + ":", v])
            difference_list.append(["  +", k + ":", file2[k]])
            file2.pop(k)
            continue

    for k, v in file2.items():
        difference_list.append(["  +", k + ":", v])

    sort_list = sorted(difference_list, key=lambda x: x[1])
    new = list(map(
            lambda x: [x[0], x[1], str(x[2]).lower() if type(x[2]) == bool else str(x[2])],  # noqa: E501
            sort_list))
    answer_list = "\n".join(["{"] + [" ".join(x) for x in new] + ["}"])

    print(answer_list)


def main():
    generate_diff("file1.json", "file2.json")


if __name__ == "__main__":
    main()
