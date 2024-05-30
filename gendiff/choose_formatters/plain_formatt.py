def to_str(value):
    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    elif value == None:
        return 'null'
    else:
        return f"'{value}'"


def get_plain_formatt(tree, res_stroka='', res = []):
    for key in tree:
        stroka = ''
        if tree[key]['status'] == 'nested':
            stroka = res_stroka + str(key) + '.'
            get_plain_formatt(tree[key]['value'], stroka)
        elif tree[key]['status'] == 'add':
            stroka = res_stroka + str(key)
            if type(tree[key]['value']) is dict:
                res.append(f"Property '{stroka}' was added with value: [complex value]")
            else:
                res.append(f"Property '{stroka}' was added with value: {to_str(tree[key]['value'])}")
        elif tree[key]['status'] == 'delete':
            stroka = res_stroka + str(key)
            res.append(f"Property '{stroka}' was removed")
        elif tree[key]['status'] == 'change':
            stroka = res_stroka + str(key)
            if type(tree[key]['old_value']) is dict and type(tree[key]['new_value']) is not dict:
                res.append(f"Property '{stroka}' was updated. From [complex value] to {to_str(tree[key]['new_value'])}")
            elif type(tree[key]['old_value']) is not dict and type(tree[key]['new_value']) is dict:
                res.append(f"Property '{stroka}' was updated. From {to_str(tree[key]['old_value'])} to [complex value]")
            elif type(tree[key]['old_value']) is not dict and type(tree[key]['old_value']) is not dict:
                res.append(f"Property '{stroka}' was updated. From {to_str(tree[key]['old_value'])} to {to_str(tree[key]['new_value'])}")
        elif tree[key]['status'] == 'unchange':
            pass
    return res

def get_result_plain_formatt(tree):
    return '\n'.join(get_plain_formatt(tree))
