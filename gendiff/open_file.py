import json
import yaml

def get_open_file_json(file_path):
    file = json.load(open(file_path, 'r'))
    return file


def get_open_file_yaml(file_path):
    file = yaml.full_load(open(file_path, 'r'))
    return file
