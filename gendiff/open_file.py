import json
import yaml
import os


FILE_EXTENSIONS_JSON = ('json')
FILE_EXTENSIONS_YAML = ('yaml', 'yml')


def parse_json(file_path):
    file = json.load(open(file_path, 'r'))
    return file


def parse_yaml(file_path):
    file = yaml.safe_load(open(file_path, 'r'))
    return file


def get_extensions_file(file_path):
    _, permission = os.path.splitext(file_path)
    if permission[1:] in FILE_EXTENSIONS_JSON:
        return parse_json(file_path)
    elif permission[1:] in FILE_EXTENSIONS_YAML:
        return parse_yaml(file_path)
    else:
        return 'The file is selected incorrectly!'
