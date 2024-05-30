import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path_1, file_path_2, formatter, result_file_path", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish', 'tests/fixtures/result_file1_file2.txt'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'stylish', 'tests/fixtures/result_file1_file2.txt'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'stylish', 'tests/fixtures/result_file3_file4.txt'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'stylish', 'tests/fixtures/result_file3_file4.txt'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'plain', 'tests/fixtures/result_plain_format.txt'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'plain', 'tests/fixtures/result_plain_format.txt'),
])
def test_generate_diff(file_path_1, file_path_2, formatter, result_file_path):
    with open(result_file_path, 'r') as file:
        exp_result = file.read()
    assert generate_diff(file_path_1, file_path_2, formatter) == exp_result
