def to_str(value):
    values = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    if type(value) is int:
        return str(value)
    elif isinstance(value, dict):
        return value
    elif value in values:
        return values[value]
    else:
        return f"'{str(value)}'"


def old_val(tree):
    return tree['old_value']


def new_val(tree):
    return tree['new_value']


def get_compar(tree):
    return isinstance(tree, dict)


def get_list_status_add(tree, strs=''):
    resl = []
    if get_compar(tree['value']):
        resl.append(
            f"Property '{strs}' was added "
            f"with value: [complex value]")
    else:
        resl.append(
            f"Property '{strs}' was added "
            f"with value: {to_str(tree['value'])}")
    return resl


def get_list_status_change(tree, strs=''):
    res = []
    if type(old_val(tree)) is dict and type(new_val(tree)) is not dict:
        res.append(
            f"Property '{strs}' was updated. "
            f"From [complex value] "
            f"to {to_str(tree['new_value'])}")
    elif type(old_val(tree)) is not dict and type(new_val(tree)) is dict:
        res.append(
            f"Property '{strs}' was updated. "
            f"From {to_str(tree['old_value'])} "
            f"to [complex value]")
    elif type(old_val(tree)) is not dict and type(new_val(tree)) is not dict:
        res.append(
            f"Property '{strs}' was updated. "
            f"From {to_str(tree['old_value'])} "
            f"to {to_str(tree['new_value'])}")
    elif type(old_val(tree)) is dict and type(new_val(tree)) is dict:
        res.append(
            f"Property '{strs}' was updated. "
            f"From [complex value] "
            f"to [complex value]")
    return res


def get_plain_formatt(tree, res_stroka='', ):
    res = []
    for key in tree:
        stroka = ''
        match tree[key]['status']:
            case 'nested':
                stroka = res_stroka + str(key) + '.'
                res.extend(get_plain_formatt(tree[key]['value'], stroka))
            case 'add':
                stroka = res_stroka + str(key)
                res.extend(get_list_status_add(tree[key], stroka))
            case 'delete':
                stroka = res_stroka + str(key)
                res.append(f"Property '{stroka}' was removed")
            case 'change':
                stroka = res_stroka + str(key)
                res.extend(get_list_status_change(tree[key], stroka))
            case 'unchange':
                pass
    return res


def get_result_plain_formatt(tree):
    return '\n'.join(get_plain_formatt(tree))
