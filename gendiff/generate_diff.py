from open_file import get_open_file_json, get_open_file_yaml
from gendiff.formaters.format import choose_format
from parsing import get_finding_diff

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
    parsing = get_finding_diff(first_file, second_file)
    result = choose_format(parsing, stylish)
    return '{' + '\n' + '\n'.join(result)+ '\n' + '}'



print(generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json'))
# print(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml'))