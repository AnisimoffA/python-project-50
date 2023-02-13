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

        count = 0
        need = len(current_value)
        for k, meta in current_value.items():
            count += 1
            if k == "mark":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"mark": "{meta}"{comma}')
                continue
            elif k == "value":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"value": {iter_(meta, deep_size)}{comma}') #  noqa
                continue

            if meta["mark"] != "+" and meta["mark"] != "-":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)}{comma}') #  noqa
            else:
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)}{comma}') #  noqa

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)


def comma_check(counter, predict):
    if counter == predict:
        return ""
    return ","
