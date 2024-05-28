import json
import yaml

def get_open_file_json(file_path):
    file = json.load(open(file_path, 'r'))
    return file


def get_open_file_yaml(file_path):
    file = yaml.full_load(open(file_path, 'r'))
    return file


# #a, b = get_open_file_json('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
# print(get_open_file_json('tests/fixtures/file1.json'))
# print(get_open_file_json('tests/fixtures/file2.json'))
# # print(get_open_file_yaml('tests/fixtures/file3.yaml'))
# print(get_open_file_yaml('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml'))
#print(type(get_open_file_yaml('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')))