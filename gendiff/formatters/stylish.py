import itertools


def to_stylish(value, replacer='    ', depth=1):  # noqa C901

    def iter_(current_value, depth):
        new_depth = depth + 1
        space = replacer * depth
        space_for_last_string = (depth - 1) * replacer
        lines = []

        for value in current_value:
            if value["status"] == "changed":
                format_old = formatted_value(value.get('old_value'), new_depth)
                format_new = formatted_value(value.get('new_value'), new_depth)
                lines.append(f"{space[:-2]}- {value['key']}: {format_old}")
                lines.append(f"{space[:-2]}+ {value['key']}: {format_new}")

            if value["status"] == "nested":
                new_data = formatted_value(value.get('changes'), new_depth)
                lines.append(f"{space}{value['key']}: {new_data}")

            if value["status"] == "same":
                new_data = formatted_value(value.get('changes'), new_depth)
                lines.append(f"{space}{value['key']}: {new_data}")

            if value["status"] == "added":
                mark = "+" if value["status"] == "added" else "-"
                new_data = formatted_value(value.get('changes'), new_depth)
                lines.append(f"{space[:-2]}{mark} {value['key']}: {new_data}")

            if value["status"] == "removed":
                mark = "+" if value["status"] == "added" else "-"
                new_data = formatted_value(value.get('changes'), new_depth)
                lines.append(f"{space[:-2]}{mark} {value['key']}: {new_data}")

        result = itertools.chain("{", lines, [space_for_last_string + "}"])
        return '\n'.join(result)
    return iter_(value, depth)


def formatted_value(data, depth):
    replacer = '    '
    space = replacer * depth
    space_for_last_string = (depth - 1) * replacer
    lines = []

    if isinstance(data, dict):
        for key, val in data.items():
            lines.append(f'{space}{key}: {formatted_value(val, depth+1)}')
        result = itertools.chain("{", lines, [space_for_last_string + "}"])
        return '\n'.join(result)
    elif isinstance(data, list):
        return to_stylish(data, depth=depth)
    else:
        if isinstance(data, bool):
            return 'true' if data else 'false'
        elif data is None:
            return 'null'
        return data
