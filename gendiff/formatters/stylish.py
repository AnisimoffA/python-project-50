import itertools

def stylish(value, replacer=' ', spaces_count=4):  # noqa C901

    def iter_(current_value, depth):
        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []

        if isinstance(current_value, dict):
            for k, v in current_value.items():
                lines.append(f'{deep_indent}{k}: {iter_(v, deep_size)}')

        if not isinstance(current_value, list) and not isinstance(current_value, dict):  # noqa E501
            return str(current_value)

        if isinstance(current_value, list):
            for v in current_value:
                if v["status"] == "changed":
                    lines.append(f'{deep_indent[:-2]}- {v["key"]}: {iter_((v["old_value"]), deep_size)}')  # noqa E501
                    lines.append(f'{deep_indent[:-2]}+ {v["key"]}: {iter_((v["new_value"]), deep_size)}')  # noqa E501
                if v["status"] == "nested" or v["status"] == "same":
                    lines.append(f'{deep_indent}{v["key"]}: {iter_(v["changes"], deep_size)}')  # noqa E501
                if v["status"] == "added" or v["status"] == "removed":
                    mark = "+" if v["status"] == "added" else "-"
                    lines.append(f'{deep_indent[:-2]}{mark} {v["key"]}: {iter_(v["changes"], deep_size)}')  # noqa E501

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
