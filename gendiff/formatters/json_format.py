from gendiff.interface import local_formater, json_format_dict
import itertools


def json_format(value, replacer=' ', spaces_count=4):  # noqa
    value = json_format_dict(value)

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return local_formater(current_value, "json_format")

        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []
        for k, meta in current_value.items():
            if k == "mark":
                lines.append(f'{deep_indent}"mark": "{meta}",')
                continue
            elif k == "value":
                lines.append(f'{deep_indent}"value": {iter_(meta, deep_size)},')
                continue

            if meta["mark"] != "+" and meta["mark"] != "-":
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)},')
            else:
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)},')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
