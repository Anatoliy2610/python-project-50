def build_tree(dict1, dict2):
    shared_keys = set(dict1) | set(dict2)
    res = {}
    for key in sorted(shared_keys):
        if key not in dict1:
            res[key] = {'status': 'add',
                        'value': dict2[key]
                        }
        elif key not in dict2:
            res[key] = {'status': 'delete',
                        'value': dict1[key]
                        }
        elif dict1[key] == dict2[key]:
            res[key] = {'status': 'unchange',
                        'value': dict1[key]
                        }
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            res[key] = {'status': 'nested',
                        'value': build_tree(dict1[key], dict2[key])
                        }
        else:
            res[key] = {'status': 'change',
                        'old_value': dict1[key],
                        'new_value': dict2[key]
                        }

    return res
