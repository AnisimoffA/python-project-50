import itertools


def stylish(value, replacer=' ', spaces_count=4):  # noqa

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []

        for k, v in current_value.items():
            if v["status"] == "changed":
                lines.append(f'{deep_indent[:-2]}- {k}: {iter_((v["old_value"]), deep_size)}')  # noqa
                lines.append(f'{deep_indent[:-2]}+ {k}: {iter_((v["new_value"]), deep_size)}')  # noqa
            if v["status"] == "nested" or v["status"] == "same":
                lines.append(f'{deep_indent}{k}: {iter_(v["changes"], deep_size)}')  # noqa
            if v["status"] == "added" or v["status"] == "removed":
                mark = "+" if v["status"] == "added" else "-"
                lines.append(f'{deep_indent[:-2]}{mark} {k}: {iter_(v["changes"], deep_size)}')  # noqa

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
