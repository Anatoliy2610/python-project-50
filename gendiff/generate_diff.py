from open_file import get_sorted_file_json, get_sorted_file_yaml
from parsing import get_parsing


def generate_diff(file1_path, file2_path):
    name_first_file = file1_path
    if name_first_file[-2] == 'o':
        first_file, second_file = get_sorted_file_json(file1_path, file2_path)
    if name_first_file[-2] == 'm':
        first_file, second_file = get_sorted_file_yaml(file1_path, file2_path)
    parsing = get_parsing(first_file, second_file)
    result = '{' + '\n' + '\n'.join(parsing)+ '\n' + '}'
    return result



#print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
#print(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml'))