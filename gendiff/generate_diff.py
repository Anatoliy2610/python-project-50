from gendiff.choose_formatters.choose_formatt import choose_formatt
from gendiff.open_file import get_file_permission
from gendiff.compare_trees import compare_trees


def generate_diff(file1_path, file2_path, stylish='stylish'):
    first_file = get_file_permission(file1_path)
    second_file = get_file_permission(file2_path)
    parsing = compare_trees(first_file, second_file)
    result = choose_formatt(parsing, stylish)
    return result
