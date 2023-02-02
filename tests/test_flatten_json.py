from gendiff import diff_gen
from true_answers import TRUE_FLATTEN
from gendiff.formatters import stylish


def test_flatten_json():
    needed_diff = diff_gen.generate_diff("flatten_before.json","flatten_after.json") # noqa: E501
    stylish_diff = stylish.stylish(needed_diff)
    assert stylish_diff == TRUE_FLATTEN

a = diff_gen.generate_diff("flatten_before.json","flatten_after.json")

print(stylish.stylish(a) == TRUE_FLATTEN)