from gendiff.interface import local_formater
import itertools


def plain(item):  # noqa C901

    def inside(item, ancestry):
        lines = []

        for v in item:
            if v["status"] == "changed":
                old = local_formater(v["old_value"], "plain")
                new = local_formater(v["new_value"], "plain")
                lines.append(f"Property '{ancestry}{v['key']}' was updated. From {old} to {new}")  # noqa E501
            elif v["status"] == "added":
                v2 = local_formater(v['changes'], "plain")
                lines.append(f"Property '{ancestry}{v['key']}' was added with value: {v2}")  # noqa E501
            elif v["status"] == "removed":
                lines.append(f"Property '{ancestry}{v['key']}' was removed")
            elif v["status"] == "nested" or v["status"] == "same":
                if isinstance(v['changes'], list):
                    ancestry += v['key']
                    lines.append(inside(v['changes'], ancestry + "."))
                    ancestry = ancestry.replace(v['key'], "")
        result = itertools.chain(lines)
        return "\n".join(result)
    return inside(item, "")
