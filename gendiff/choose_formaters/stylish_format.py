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


def stylish_format(tree, depth=0, symbol=' '):
    indent = symbol * NUM_SYMBOLS * depth
    resl = []
    for key in tree:
        if isinstance(tree[key], dict):
            if 'status' in tree[key]:
                status = tree[key]['status']
                match status:
                    case 'nested':
                        value = tree[key]['value']
                        resl.append(f'{indent}    {key}: ' + '{')
                        resl.extend(stylish_format(value, depth + 1))
                        resl.append(f'{indent}    ' + '}')
                    case 'add':
                        value = tree[key]['value']
                        if isinstance(tree[key]['value'], dict):
                            resl.append(f'{indent}  + {key}: ' + '{')
                            resl.extend(stylish_format(value, depth + 1))
                            resl.append(f'{indent}    ' + '}')
                        else:
                            resl.append(f'{indent}  + {key}: {to_str(value)}')
                    case 'delete':
                        value = tree[key]['value']
                        if isinstance(tree[key]['value'], dict):
                            resl.append(f'{indent}  - {key}: ' + '{')
                            resl.extend(stylish_format(value, depth + 1))
                            resl.append(f'{indent}    ' + '}')
                        else:
                            resl.append(f'{indent}  - {key}: {to_str(value)}')
                    case 'change':
                        old_val = tree[key]['old_value']
                        new_val = tree[key]['new_value']
                        if isinstance(old_val, dict):
                            resl.append(f'{indent}  - {key}: ' + '{')
                            resl.extend(stylish_format(old_val, depth + 1))
                            resl.append(f'{indent}    ' + '}')
                        else:
                            resl.append(f'{indent}  - {key}: {to_str(old_val)}')
                        if isinstance(new_val, dict):
                            resl.append(f'{indent}  + {key}: ' + '{')
                            resl.extend(stylish_format(new_val, depth + 1))
                            resl.append(f'{indent}    ' + '}')
                        else:
                            resl.append(f'{indent}  + {key}: {to_str(new_val)}')
                    case 'unchange':
                        value = tree[key]['value']
                        if isinstance(value, dict):
                            resl.append(f'{indent}    {key}: ' + '{')
                            resl.extend(stylish_format(value, depth + 1))
                            resl.append(f'{indent}    ' + '}')
                        else:
                            resl.append(f'{indent}    {key}: {to_str(value)}')
            else:
                resl.append(f'{indent}    {key}: ' + '{')
                resl.extend(stylish_format(tree[key], depth + 1))
                resl.append(f'{indent}    ' + '}')
        else:
            resl.append(f'{indent}    {key}: {to_str(tree[key])}')
    return resl


def get_result_stylish_format(tree):
    return '{' + '\n' + '\n'.join(stylish_format(tree)) + '\n' + '}'
