import itertools


def to_plain(item):  # noqa C901

    def inside(item, ancestry):
        lines = []

        for value in item:
            if value["status"] == "changed":
                old = local_formater(value["old_value"], "plain")
                new = local_formater(value["new_value"], "plain")
                lines.append(f"Property '{ancestry}{value['key']}' was updated. From {old} to {new}")  # noqa E501
            elif value["status"] == "added":
                changed_value = local_formater(value['changes'], "plain")
                lines.append(f"Property '{ancestry}{value['key']}' was added with value: {changed_value}")  # noqa E501
            elif value["status"] == "removed":
                lines.append(f"Property '{ancestry}{value['key']}' was removed")
            elif value["status"] == "nested" or value["status"] == "same":
                if isinstance(value['changes'], list):
                    ancestry += value['key']
                    lines.append(inside(value['changes'], ancestry + "."))
                    ancestry = ancestry.replace(value['key'], "")
        result = itertools.chain(lines)
        return "\n".join(result)
    return inside(item, "")


def local_formater(item, format):
    if not isinstance(item, dict):
        if item == "false" or item == "true" or item == "null":
            return item
        if isinstance(item, int):
            return item
        return f"\'{item}\'" if format == "plain" else f"\"{item}\""
    return "[complex value]"
