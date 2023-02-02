from gendiff import diff_gen
from true_answers import TRUE_NONFLATTEN
from gendiff.formatters import stylish


def test_flatten_json():
    needed_diff = diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json") # noqa: E501
    stylish_diff = stylish.stylish(needed_diff)
    assert stylish_diff == TRUE_NONFLATTEN
