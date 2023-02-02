from gendiff import diff_gen
from true_answers import TRUE_NONFLATTEN


def test_nonflatten_json():
    needed_diff = diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json") # noqa: E501
    assert needed_diff == TRUE_NONFLATTEN
