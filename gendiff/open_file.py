import json
import yaml
import os


FILE_EXTENSIONS_JSON = 'json'
FILE_EXTENSIONS_YAML = 'yaml, yml'


def get_permission_file(file_path):
    data_file = open(file_path, 'r')
    _, permission = os.path.splitext(file_path)
    return data_file, permission.replace('.', '')


def parse_data(data_file, permission):
    if permission in FILE_EXTENSIONS_JSON:
        return json.load(data_file)
    elif permission in FILE_EXTENSIONS_YAML:
        return yaml.safe_load(data_file)
    else:
        return 'The file is selected incorrectly!'
