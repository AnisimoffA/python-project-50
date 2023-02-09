import itertools
from gendiff.interface import to_sorted_dict, mark_form


def stylish(value, replacer=' ', spaces_count=4):  # noqa
    new_value = to_sorted_dict(value)

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []
        for key, v in current_value.items():
            if "change" in key:
                key = mark_form(key)
            if key[0] != "+" and key[0] != "-":
                lines.append(f'{deep_indent}{key}: {iter_(v, deep_size)}')
            else:
                lines.append(f'{deep_indent[:-2]}{key}: {iter_(v, deep_size)}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(new_value, 0)
