from gendiff import diff_gen
from true_answers import TRUE_FLATTEN


def test_flatten_json():
    needed_diff = diff_gen.generate_diff("flatten_before.json","flatten_after.json") # noqa: E501
    assert needed_diff == TRUE_FLATTEN

print(diff_gen.generate_diff("flatten_before.json","flatten_after.json"))