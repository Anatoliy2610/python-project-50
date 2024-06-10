import json
import yaml
import os


FILE_EXTENSIONS_JSON = 'json'
FILE_EXTENSIONS_YAML = 'yaml'
FILE_EXTENSIONS_YML = 'yml'


def get_extension_file(file_path):
    open_file = open(file_path, 'r')
    _, file_extension = os.path.splitext(file_path)
    return open_file, file_extension.replace('.', '')


def parse_data(open_file, file_extension):
    if file_extension == FILE_EXTENSIONS_JSON:
        return json.load(open_file)
    elif file_extension == FILE_EXTENSIONS_YAML:
        return yaml.safe_load(open_file)
    elif file_extension == FILE_EXTENSIONS_YML:
        return yaml.safe_load(open_file)
    else:
        return 'The file is selected incorrectly!'


def get_data_file(file_path1, file_path2):
    open_file1, file_extension1 = get_extension_file(file_path1)
    open_file2, file_extension2 = get_extension_file(file_path2)
    data_file1 = parse_data(open_file1, file_extension1)
    data_file2 = parse_data(open_file2, file_extension2)
    return data_file1, data_file2
