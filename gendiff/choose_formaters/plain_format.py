def to_str(value):
    values = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    if type(value) is int:
        return str(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif value in values:
        return values[value]
    else:
        return f"'{str(value)}'"


def plain_format(tree, name_dir=''):
    result = []
    for key in tree:
        name_key = ''
        match tree[key]['status']:
            case 'nested':
                name_key = name_dir + str(key) + '.'
                result.extend(plain_format(tree[key]['value'], name_key))
            case 'add':
                name_key = name_dir + str(key)
                result.append(
                    f"Property {to_str(name_key)} "
                    f"was added with value: {to_str(tree[key]['value'])}")
            case 'delete':
                name_key = name_dir + str(key)
                result.append(
                    f"Property {to_str(name_key)} was removed")
            case 'change':
                name_key = name_dir + str(key)
                result.append(
                    f"Property {to_str(name_key)} was updated. "
                    f"From {to_str(tree[key]['old_value'])} "
                    f"to {to_str(tree[key]['new_value'])}")
            case 'unchange':
                pass
    return result


def get_result_plain_format(tree):
    return '\n'.join(plain_format(tree))
