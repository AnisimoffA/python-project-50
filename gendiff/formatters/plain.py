import itertools
from gendiff.interface import none_to_null

def to_plain(item):  # noqa C901
    item = none_to_null(item)
    def inside(item, ancestry):
        lines = []

        for value in item:
            if value["status"] == "changed":
                old = local_formater(value["old_value"])
                new = local_formater(value["new_value"])
                lines.append(f"Property '{ancestry}{value['key']}' was updated. From {old} to {new}")  # noqa E501
            elif value["status"] == "added":
                changed_value = local_formater(value['changes'])
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


def local_formater(item):
    if not isinstance(item, dict):
        if item == "false" or item == "true" or item == "null":
            return item
        if isinstance(item, int):
            return item
        return f"\'{item}\'"
    return "[complex value]"
