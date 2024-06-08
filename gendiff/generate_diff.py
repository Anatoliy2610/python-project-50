from gendiff.build_tree import build_tree
from gendiff.choose_formaters.choose_format import choose_format
from gendiff.open_file import parse_data, get_permission_file


def generate_diff(file1_path, file2_path, stylish='stylish'):
    data_file1, permission_file1 = get_permission_file(file1_path)
    data_file2, permission_file2 = get_permission_file(file2_path)
    first_file = parse_data(data_file1, permission_file1)
    second_file = parse_data(data_file2, permission_file2)
    tree = build_tree(first_file, second_file)
    result = choose_format(tree, stylish)
    return result
