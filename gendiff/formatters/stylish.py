import itertools
from gendiff.interface import none_to_null


def to_stylish(value, replacer='    ', depth=1):
    value = none_to_null(value)

    def iter_(current_value, depth):
        new_depth = depth + 1
        actual_space = replacer * depth
        space_for_last_string = (depth-1) * replacer
        lines = []

        for value in current_value:
            if value["status"] == "changed":
                format_old = formatted_value(value.get('old_value'), new_depth)
                format_new = formatted_value(value.get('new_value'), new_depth)
                lines.append(f"{actual_space[:-2]}- {value['key']}: {format_old}")
                lines.append(f"{actual_space[:-2]}+ {value['key']}: {format_new}")

            if value["status"] == "nested":
                lines.append(f"{actual_space}{value['key']}: {formatted_value(value.get('changes'), new_depth)}")

            if value["status"] == "same":
                lines.append(f"{actual_space}{value['key']}: {formatted_value(value.get('changes'), new_depth)}")

            if value["status"] == "added" or value["status"] == "removed":
                mark = "+" if value["status"] == "added" else "-"
                format_value = formatted_value(value.get('changes'), new_depth)
                lines.append(f"{actual_space[:-2]}{mark} {value['key']}: {format_value}")

        result = itertools.chain("{", lines, [space_for_last_string + "}"])
        return '\n'.join(result)
    return iter_(value, depth)


def formatted_value(data, depth):
    replacer = '    '
    actual_space = replacer * depth
    space_for_last_string = (depth-1) * replacer
    lines = []

    if isinstance(data, int) or isinstance(data, str):
        return data
    if isinstance(data, dict):
        for key, val in data.items():
            lines.append(f'{actual_space}{key}: {formatted_value(val, depth+1)}')
        result = itertools.chain("{", lines, [space_for_last_string + "}"])
        return '\n'.join(result)
    if isinstance(data, list):
        return to_stylish(data, depth=depth)