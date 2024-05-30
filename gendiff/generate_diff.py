from gendiff.choose_formatters.choose_formatt import choose_formatt
from gendiff.open_file import get_open_file_json, get_open_file_yaml
from gendiff.compare_trees import compare_trees


def generate_diff(file1_path, file2_path, stylish='stylish'):
    if file1_path[-4:] == 'json' and file2_path[-4:] == 'json':
        first_file = get_open_file_json(file1_path)
        second_file = get_open_file_json(file2_path)
    if file1_path[-4:] == 'yaml' and file2_path[-4:] == 'yaml':
        first_file = get_open_file_yaml(file1_path)
        second_file = get_open_file_yaml(file2_path)
    if file1_path[-3:] == 'yml' and file2_path[-3:] == 'yml':
        first_file = get_open_file_yaml(file1_path)
        second_file = get_open_file_yaml(file2_path)
    parsing = compare_trees(first_file, second_file)
    result = choose_formatt(parsing, stylish)
    return result
