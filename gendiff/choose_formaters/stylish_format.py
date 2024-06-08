NUM_SYMBOLS = 4


def to_str(value):
    values = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    if type(value) is int:
        return str(value)
    elif value in values:
        return values[value]
    else:
        return str(value)


def walk_to_one_tree(tree, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    res = []
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{indent}    {key}: ' + '{')
            res.extend(walk_to_one_tree(tree[key], depth + 1))
            res.append(f'{indent}    ' + '}')
        else:
            res.append(f'{indent}    {to_str(key)}: {to_str(tree[key])}')
    return res


def get_value_delete(tree, key, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  - {to_str(key)}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  - {to_str(key)}: {to_str(tree['value'])}")
    return res


def get_value_add(tree, key, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  + {key}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  + {key}: {to_str(tree['value'])}")
    return res


def get_change(value, depth=1, symbol=' ', res=''):
    indent = symbol * NUM_SYMBOLS * depth
    if isinstance(value, dict):
        for key in value:
            res = res + '{' + '\n' + indent + '    ' + to_str(key) + ': '
            res = res + get_change(value[key], depth + 1) + '\n' + indent + '}'
    else:
        return to_str(value)
    return res


def get_value_change(tree, key, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    res = []
    old_value = tree['old_value']
    new_value = tree['new_value']
    res.append(f"{indent}  - {key}: {get_change(old_value, depth + 1)}")
    res.append(f"{indent}  + {key}: {get_change(new_value, depth + 1)}")
    return res


def get_value_unchange(tree, key, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    result = []
    result.append(
        f"{indent}    {to_str(key)}: "
        f"{to_str(tree)}")
    return result


def get_stylish_format(tree, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    res = []
    for key in tree:
        match tree[key]['status']:
            case 'nested':
                res.append(f"{indent}    {key}: " + '{')
                res.extend(get_stylish_format(tree[key]['value'], depth + 1))
                res.append(f"{indent}    " + '}')
            case 'add':
                res.extend(get_value_add(tree[key], key, depth))
            case 'delete':
                res.extend(get_value_delete(tree[key], key, depth))
            case 'change':
                res.extend(get_value_change(tree[key], key, depth))
            case 'unchange':
                res.extend(get_value_unchange(tree[key]['value'], key, depth))
    return res


def get_result_stylish_format(tree):
    return '{' + '\n' + '\n'.join(get_stylish_format(tree)) + '\n' + '}'
