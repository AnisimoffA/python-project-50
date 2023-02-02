from gendiff import diff_gen
from true_answers import TRUE_FLATTEN


def test_flatten_jaml():
    needed_diff = diff_gen.generate_diff("flatten_before.jaml","flatten_after.jaml") # noqa: E501
    assert needed_diff == TRUE_FLATTEN
