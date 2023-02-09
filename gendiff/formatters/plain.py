import itertools
from gendiff.interface import to_sorted_list, find_changed_values, local_formater  # noqa


def plain(item):  # noqa
    item = to_sorted_list(item)

    def inside(item, ancestry):
        lines = []
        updated_item = find_changed_values(item)

        for mark, k, v in updated_item:
            v2 = local_formater(v)
            if mark == "+":
                lines.append(f"Property \'{ancestry}{k}\' was added with value: {v2}")  # noqa
            elif mark == "-":
                lines.append(f"Property \'{ancestry}{k}\' was removed")
            elif mark == "":
                if isinstance(v, list):
                    ancestry += k
                    lines.append(inside(v, ancestry + "."))
                    ancestry = ancestry.replace(k, "")
            else:
                old = local_formater(v["old"])
                new = local_formater(v["new"])
                lines.append(f"Property \'{ancestry}{k}\' was updated. From {old} to {new}")  # noqa

        result = itertools.chain(lines)
        return "\n".join(result)
    return inside(item, "")
