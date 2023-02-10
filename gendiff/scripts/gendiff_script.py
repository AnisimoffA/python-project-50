#!/usr/bin/env python3
import argparse
from gendiff.diff_gen import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_format


def main():
    parser = argparse.ArgumentParser()

    # позиционные
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # опциональные
    parser.add_argument("-f", "--format", help="set format of output", default="stylish")  # noqa: E501

    args = parser.parse_args()

    if args.format == "stylish":
        answer = generate_diff(args.first_file, args.second_file, stylish)
        print(answer)
    elif args.format == "plain":
        answer = generate_diff(args.first_file, args.second_file, plain)
        print(answer)
    elif args.format == "json_format":
        answer = generate_diff(args.first_file, args.second_file, json_format)
        print(answer)
    else:
        print("something went wrong")


if __name__ == "__main__":
    main()
