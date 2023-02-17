from gendiff.interface import local_formater
import itertools


def plain(item):  # noqa
    def inside(item, ancestry):
        lines = []

        for k, v in item.items():
            if v["status"] == "changed":
                old = local_formater(v["old_value"], "plain")
                new = local_formater(v["new_value"], "plain")
                lines.append(f"Property \'{ancestry}{k}\' was updated. From {old} to {new}")  # noqa
            elif v["status"] == "added":
                v2 = local_formater(v['changes'], "plain")
                lines.append(f"Property \'{ancestry}{k}\' was added with value: {v2}")  # noqa
            elif v["status"] == "removed":
                lines.append(f"Property \'{ancestry}{k}\' was removed")
            elif v["status"] == "nested" or v["status"] == "same":
                if isinstance(v['changes'], dict):
                    ancestry += k
                    lines.append(inside(v['changes'], ancestry + "."))
                    ancestry = ancestry.replace(k, "")
        result = itertools.chain(lines)
        return "\n".join(result)
    return inside(item, "")
