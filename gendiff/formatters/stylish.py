import itertools
from gendiff.interface import none_to_null


def to_stylish(value, replacer=' ', spaces_count=4):  # noqa C901
    value = none_to_null(value)
    def iter_(current_value, depth):
        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []
        if isinstance(current_value, dict):
            for key, value in current_value.items():
                lines.append(f'{deep_indent}{key}: {iter_(value, deep_size)}')

        if not isinstance(current_value, list) and not isinstance(current_value, dict):  # noqa E501
            return str(current_value)

        if isinstance(current_value, list):
            for value in current_value:
                if value["status"] == "changed":
                    lines.append(f'{deep_indent[:-2]}- {value["key"]}: {iter_((value["old_value"]), deep_size)}')  # noqa E501
                    lines.append(f'{deep_indent[:-2]}+ {value["key"]}: {iter_((value["new_value"]), deep_size)}')  # noqa E501
                if value["status"] == "nested" or value["status"] == "same":
                    lines.append(f'{deep_indent}{value["key"]}: {iter_(value["changes"], deep_size)}')  # noqa E501
                if value["status"] == "added" or value["status"] == "removed":
                    mark = "+" if value["status"] == "added" else "-"
                    lines.append(f'{deep_indent[:-2]}{mark} {value["key"]}: {iter_(value["changes"], deep_size)}')  # noqa E501

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
