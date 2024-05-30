def to_str(value):
    values = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    if value in values:
        return values[value]
    else:
        return str(value).lower()


def get_value_delete(tree, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  - {to_str(tree)}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  - {to_str(tree)}: {to_str(tree['value'])}")
    return res


def get_value_add(tree, depth=0, symbol=' ', num_symbols=4):
    indent = symbol * num_symbols * depth
    res = []
    if isinstance(tree['value'], dict):
        res.append(f"{indent}  + {to_str(tree)}: " + '{')
        res.extend(walk_to_one_tree(tree['value'], depth + 1))
        res.append(f"{indent}    " + '}')
    else:
        res.append(f"{indent}  + {to_str(tree)}: {to_str(tree['value'])}")
    return res


def get_value_change():
    pass


def walk_to_one_tree(tree, depth=0, symbol=' ', num_symbols=4, res=[]):
    indent = symbol * num_symbols * depth
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{indent}    {to_str( key)}: ' + '{')
            walk_to_one_tree(tree[key], depth + 1)
            res.append(f'{indent}    ' + '}')
        else:
            res.append(f'{indent}    {to_str(key)}: {to_str(tree[key])}')
    return res


def get_stylish_formatt(tree, depth=0, symbol=' ', num_symbols=4, res=[]):
    indent = symbol * num_symbols * depth
    for key in tree:
        match tree[key]['status']:
            case 'nested':
                res.append(f"{indent}    {to_str(key)}: " + '{')
                get_stylish_formatt(tree[key]['value'], depth + 1)
                res.append(f"{indent}    " + '}')
            case 'add':
                res.extend(get_value_add(tree[key]['value'], depth))
            case 'delete':
                res.extend(get_value_delete(tree[key]['value'], depth))
            case 'change':
                res.append(
                    f"{indent}  - {to_str(key)}: "
                    f"{to_str(tree[key]['old_value'])}")
                res.append(
                    f"{indent}  + {to_str(key)}: "
                    f"{to_str(tree[key]['new_value'])}")
            case 'unchange':
                res.append(
                    f"{indent}    {to_str(key)}: "
                    f"{to_str(tree[key]['value'])}")
    return res


def get_result_stylish_formatt(tree):
    return '{' + '\n' + '\n'.join(get_stylish_formatt(tree)) + '\n' + '}'
