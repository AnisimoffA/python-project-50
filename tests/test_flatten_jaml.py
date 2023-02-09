from gendiff import diff_gen
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_format
from true_answers import TRUE_FLATTEN, TRUE_FLATTEN_PLAIN, TRUE_FLATTEN_JSON_FORMAT


def test_flatten_jaml():
    needed_diff_stylish = diff_gen.generate_diff("flatten_before.jaml","flatten_after.jaml", stylish)  # noqa: E501
    needed_diff_plain = diff_gen.generate_diff("flatten_before.jaml","flatten_after.jaml", plain)
    needed_diff_json_format = diff_gen.generate_diff("flatten_before.jaml","flatten_after.jaml", json_format)
    assert needed_diff_stylish == TRUE_FLATTEN
    assert needed_diff_plain == TRUE_FLATTEN_PLAIN
    assert needed_diff_json_format == TRUE_FLATTEN_JSON_FORMAT