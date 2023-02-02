from gendiff import diff_gen
from true_answers import TRUE_NONFLATTEN


def test_flatten_jaml():
    needed_diff = diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jaml") # noqa: E501
    assert needed_diff == TRUE_NONFLATTEN