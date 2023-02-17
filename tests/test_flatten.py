import pytest
from gendiff import generate_diff

params = [
    ("flatten_before.json", "flatten_after.json", "stylish", "tests/fixtures/correct_flatten_stylish.txt"),  # noqa
    ("flatten_before.json", "flatten_after.json", "plain", "tests/fixtures/correct_flatten_plain.txt"),  # noqa
    ("flatten_before.json", "flatten_after.json", "json", "tests/fixtures/correct_flatten_json.txt"),  # noqa
    ("flatten_before.jaml", "flatten_after.jaml", "stylish", "tests/fixtures/correct_flatten_stylish.txt"),  # noqa
    ("flatten_before.jaml", "flatten_after.jaml", "plain", "tests/fixtures/correct_flatten_plain.txt"),  # noqa
    ("flatten_before.jaml", "flatten_after.jaml", "json", "tests/fixtures/correct_flatten_json.txt")]  # noqa


@pytest.mark.parametrize("file1, file2, style, result", params)
def test_flatten(file1, file2, style, result):
    with open(result) as answer:
        assert generate_diff(file1, file2, style) == answer.read()
