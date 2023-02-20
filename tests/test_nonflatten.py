import pytest
from gendiff import generate_diff


json_files = ("nested_before.json", "nested_after.json")
yaml_files = ("nested_before.yml", "nested_after.yml")

params = [
    (json_files, "stylish", "tests/fixtures/correct_nested_stylish.txt"),
    (json_files, "plain", "tests/fixtures/correct_nested_plain.txt"),
    (json_files, "json", "tests/fixtures/correct_nested_json.txt"),
    (yaml_files, "stylish", "tests/fixtures/correct_nested_stylish.txt"),
    (yaml_files, "plain", "tests/fixtures/correct_nested_plain.txt"),
    (yaml_files, "json", "tests/fixtures/correct_nested_json.txt")]


@pytest.mark.parametrize("files, style, result", params)
def test_nonflatten(files, style, result):
    with open(result) as expected_result:
        file1, file2 = files
        assert generate_diff(file1, file2, style) == expected_result.read()
