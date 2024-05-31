def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return f"'{value}'"


def to_old_val(tree):
    return tree['old_value']


def to_new_val(tree):
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
    if get_compar(tree) and not get_compar(to_new_val(tree)):
        res.append(
            f"Property '{strs}' was updated. "
            f"From [complex value] "
            f"to {to_str(tree['new_value'])}")
    elif not get_compar(to_old_val(tree)) and get_compar(to_new_val(tree)):
        res.append(
            f"Property '{strs}' was updated. "
            f"From {to_str(tree['old_value'])} "
            f"to [complex value]")
    elif not get_compar(tree) and not get_compar(to_new_val(tree)):
        res.append(
            f"Property '{strs}' was updated. "
            f"From {to_str(to_old_val(tree))} "
            f"to {to_str(to_new_val(tree))}")
    return res


def get_plain_formatt(tree, res_stroka=''):
    res=[]
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
