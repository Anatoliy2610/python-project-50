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


def walk_to_one_tree(tree, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{indent}    {key}: ' + '{')
            res.extend(walk_to_one_tree(tree[key], depth + 1))
            res.append(f'{indent}    ' + '}')
        else:
            res.append(f'{indent}    {to_str(key)}: {to_str(tree[key])}')
    return res


def get_value_delete(tree, key, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  - {to_str(key)}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  - {to_str(key)}: {to_str(tree['value'])}")
    return res


def get_value_add(tree, key, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  + {key}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  + {key}: {to_str(tree['value'])}")
    return res


def get_value_change(tree, key, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    old_value = tree['old_value']
    new_value = tree['new_value']
    if not isinstance(old_value, dict) and not isinstance(new_value, dict):
        res.append(
            f"{indent}  - {to_str(key)}: "
            f"{to_str(old_value)}")
        res.append(
            f"{indent}  + {to_str(key)}: "
            f"{to_str(new_value)}")
    elif isinstance(old_value, dict) and not isinstance(new_value, dict):
        res.append(f"{indent}  - {key}: " + '{')
        res.extend(walk_to_one_tree(tree['old_value'], depth + 1))
        res.append(f"{indent}    " + '}')
        res.append(
            f"{indent}  + {to_str(key)}: "
            f"{to_str(new_value)}")
    elif not isinstance(old_value, dict) and isinstance(new_value, dict):
        res.append(
            f"{indent}  - {to_str(key)}: "
            f"{to_str(old_value)}")
        res.append(f"{indent}  + {key}: " + '{')
        res.extend(walk_to_one_tree(new_value, depth + 1))
        res.append(f"{indent}    " + '}')
    return res


def get_stylish_formatt(tree, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    for key in tree:
        match tree[key]['status']:
            case 'nested':
                res.append(f"{indent}    {key}: " + '{')
                res.extend(get_stylish_formatt(tree[key]['value'], depth + 1))
                res.append(f"{indent}    " + '}')
            case 'add':
                res.extend(get_value_add(tree[key], key, depth))
            case 'delete':
                res.extend(get_value_delete(tree[key], key, depth))
            case 'change':
                res.extend(get_value_change(tree[key], key, depth))
            case 'unchange':
                res.append(
                    f"{indent}    {to_str(key)}: "
                    f"{to_str(tree[key]['value'])}")
    return res


def get_result_stylish_formatt(tree):
    return '{' + '\n' + '\n'.join(get_stylish_formatt(tree)) + '\n' + '}'
