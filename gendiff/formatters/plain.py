def to_plain(item):  # noqa C901

    def inside(item, ancestry):
        lines = []

        for value in item:
            if value["status"] == "changed":
                old = formatted_value(value["old_value"])
                new = formatted_value(value["new_value"])
                lines.append(f"Property '{ancestry}{value['key']}' was updated. From {old} to {new}")  # noqa E501
            elif value["status"] == "added":
                changed_value = formatted_value(value['changes'])
                lines.append(f"Property '{ancestry}{value['key']}' was added with value: {changed_value}")  # noqa E501
            elif value["status"] == "removed":
                lines.append(f"Property '{ancestry}{value['key']}' was removed")
            elif value["status"] == "nested" or value["status"] == "same":
                if isinstance(value['changes'], list):
                    ancestry += value['key']
                    lines.append(inside(value['changes'], ancestry + "."))
                    ancestry = ancestry.replace(value['key'], "")
        return "\n".join(lines)
    return inside(item, "")


def formatted_value(item):
    if not isinstance(item, dict):
        if isinstance(item, bool):
            return 'true' if item else 'false'
        elif item is None:
            return 'null'
        elif item == "false" or item == "true" or item == "null":
            return item
        elif isinstance(item, int):
            return item
        return f"\'{item}\'"
    return "[complex value]"
