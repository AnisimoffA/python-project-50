import pytest
from gendiff import generate_diff

params = [
    ("nonflatten_before.json", "nonflatten_after.json", "stylish", "tests/fixtures/correct_nonflatten_stylish.txt"),
    ("nonflatten_before.json", "nonflatten_after.json", "plain", "tests/fixtures/correct_nonflatten_plain.txt"),
    ("nonflatten_before.json", "nonflatten_after.json", "json_format", "tests/fixtures/correct_nonflatten_json.txt"),
    ("nonflatten_before.jaml", "nonflatten_after.jaml", "stylish", "tests/fixtures/correct_nonflatten_stylish.txt"),
    ("nonflatten_before.jaml", "nonflatten_after.jaml", "plain", "tests/fixtures/correct_nonflatten_plain.txt"),
    ("nonflatten_before.jaml", "nonflatten_after.jaml", "json_format", "tests/fixtures/correct_nonflatten_json.txt"),
    ]

@pytest.mark.parametrize("file1, file2, style, result", params)
def test_nonflatten(file1, file2, style, result):
    with open(result) as answer:
        assert generate_diff(file1, file2, style) == answer.read()

