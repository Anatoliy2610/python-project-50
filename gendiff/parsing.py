def to_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def to_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def to_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def to_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def to_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': get_finding_diff(value1, value2)
    }


def get_finding_diff(dict1, dict2):
    shared_keys = set(dict1) | set(dict2)
    delete_keys = set(dict1) - set(dict2)
    add_keys = set(dict2) - set(dict1)
    result = {}
    for key in sorted(shared_keys):
        value_dict1 = dict1.get(key)
        value_dict2 = dict2.get(key)
        if key in delete_keys:
            result[key] = to_delete(key, value_dict1)
        elif key in add_keys:
            result[key] = to_add(key, value_dict2)
        elif type(value_dict1) is dict and type(value_dict2) is dict:
            result[key] = to_nested(key, value_dict1, value_dict2)
        elif value_dict1 != value_dict2:
            result[key] = to_modified(key, value_dict1, value_dict2)
        else:
            result[key] = to_unchanged(key, value_dict1)
    return result

