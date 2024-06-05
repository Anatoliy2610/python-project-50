from gendiff.choose_formatters.choose_format import choose_format
from gendiff.open_file import get_expansion_file
from gendiff.build_tree import build_tree


def generate_diff(file1_path, file2_path, stylish='stylish'):
    first_file = get_expansion_file(file1_path)
    second_file = get_expansion_file(file2_path)
    parsing = build_tree(first_file, second_file)
    result = choose_format(parsing, stylish)
    return result
