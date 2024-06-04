import json
import yaml
import os


def get_open_file_json(file_path):
    file = json.load(open(file_path, 'r'))
    return file


def get_open_file_yaml(file_path):
    file = yaml.safe_load(open(file_path, 'r'))
    return file


def get_file_permission(file_path):
    permission = os.path.splitext(file_path)
    if '.json' in permission:
        return get_open_file_json(file_path)
    elif '.yaml' in permission or '.yml' in permission:
        return get_open_file_yaml(file_path)
    else:
        return 'The file is selected incorrectly!'
