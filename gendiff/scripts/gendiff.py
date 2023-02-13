#!/usr/bin/env python3
import argparse
from gendiff.diff_gen import generate_diff


def main():
    parser = argparse.ArgumentParser()

    # позиционные
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # опциональные
    parser.add_argument("-f", "--format", help="set format of output", default="stylish")  # noqa: E501

    args = parser.parse_args()

    answer = generate_diff(args.first_file, args.second_file, args.format)
    print(answer)


if __name__ == "__main__":
    main()
