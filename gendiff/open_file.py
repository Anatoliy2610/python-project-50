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
    elif file_extension in (FILE_EXTENSIONS_YAML, FILE_EXTENSIONS_YML):
        return yaml.safe_load(open_file)
    else:
        return 'The file is selected incorrectly!'


def get_data_file(file_path):
    open_file, file_extension = get_extension_file(file_path)
    data_file = parse_data(open_file, file_extension)
    return data_file
