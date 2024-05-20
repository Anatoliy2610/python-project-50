import json
import yaml

def get_sorted_file_json(file1_path, file2_path):
    first_file = json.load(open(file1_path, 'r'))
    second_file = json.load(open(file2_path, 'r'))
    return first_file, second_file


def get_sorted_file_yaml(file1_path, file2_path):
    first_file1 = yaml.full_load(open(file1_path, 'r'))
    second_file1 = yaml.full_load(open(file2_path, 'r'))
    return first_file1, second_file1


#a, b = get_sorted_file_json('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
#print(get_sorted_file_json('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
#print(get_sorted_file_yaml('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml'))
#print(type(get_sorted_file_yaml('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')))