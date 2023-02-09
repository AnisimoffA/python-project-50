from gendiff import diff_gen
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_format import json_format
from true_answers import TRUE_NONFLATTEN, TRUE_NONFLATTEN_PLAIN, TRUE_NONFLATTEN_JSON_FORMAT


def test_flatten_jaml():
    needed_diff_stylish = diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json", stylish)  # noqa: E501
    needed_diff_plain = diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json", plain)
    needed_diff_json_format = diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json", json_format)
    assert needed_diff_stylish == TRUE_NONFLATTEN
    assert needed_diff_plain == TRUE_NONFLATTEN_PLAIN
    assert needed_diff_json_format == TRUE_NONFLATTEN_JSON_FORMAT