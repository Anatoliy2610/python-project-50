a = {
    'common': {'status': 'nested', 'value': {
        'follow': {'status': 'add', 'value': False}, 
        'setting1': {'status': 'unchange', 'value': 'Value 1'}, 
        'setting2': {'status': 'delete', 'value': 200}, 
        'setting3': {'status': 'change', 'old_value': True, 'new_value': None}, 
        'setting4': {'status': 'add', 'value': 'blah blah'}, 
        'setting5': {'status': 'add', 'value': {'key5': 'value5'}}, 
        'setting6': {'status': 'nested', 'value': {
            'doge': {'status': 'nested', 'value': {
                'wow': {'status': 'change', 'old_value': '', 'new_value': 'so much'}}}, 
            'key': {'status': 'unchange', 'value': 'value'}, 
            'ops': {'status': 'add', 'value': 'vops'}}}}}, 
    'group1': {'status': 'nested', 'value': {
        'baz': {'status': 'change', 'old_value': 'bas', 'new_value': 'bars'}, 
        'foo': {'status': 'unchange', 'value': 'bar'}, 
        'nest': {'status': 'change', 'old_value': {'key': 'value'}, 'new_value': 'str'}}}, 
    'group2': {'status': 'delete', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 
    'group3': {'status': 'add', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}

def to_str(value):
    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    elif value == None:
        return 'null'
    else:
        return str(value).lower()

def walk_to_one_tree(tree, depth=0, symbol=' ', num_symbols=4, res=[]):
    indent = symbol * num_symbols * depth
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{indent}    {to_str(key)}: ' + '{')
            walk_to_one_tree(tree[key], depth+1)
            res.append(f'{indent}    ' + '}')
        else:
            res.append(f'{indent}    {to_str(key)}: {to_str(tree[key])}')
    return res

def get_stylish_formatt(tree, depth=0, symbol=' ', num_symbols=4, res=[]):
    indent = symbol * num_symbols * depth
    for key in tree:
        if tree[key]['status'] == 'nested':
            res.append(f"{indent}    {to_str(key)}: " + '{')
            get_stylish_formatt(tree[key]['value'], depth+1)
            res.append(f"{indent}    " + '}')
        elif tree[key]['status'] == 'add':
            if type(tree[key]['value']) is dict:
                res.append(f"{indent}  + {to_str(key)}: " + '{')
                res.extend(walk_to_one_tree(tree[key]['value'], depth+1))
                res.append(f"{indent}    " + '}')
            else:
                res.append(f"{indent}  + {to_str(key)}: {to_str(tree[key]['value'])}")
        elif tree[key]['status'] == 'delete':
            if type(tree[key]['value']) is dict:
                res.append(f"{indent}  - {to_str(key)}: " + '{')
                res.extend(walk_to_one_tree(tree[key]['value'], depth+1))
                res.append(f"{indent}    " + '}')
            else:
                res.append(f"{indent}  - {to_str(key)}: {to_str(tree[key]['value'])}")
        elif tree[key]['status'] == 'change':
            res.append(f"{indent}  - {to_str(key)}: {to_str(tree[key]['old_value'])}")
            res.append(f"{indent}  + {to_str(key)}: {to_str(tree[key]['new_value'])}")
        elif tree[key]['status'] == 'unchange':
            res.append(f"{indent}    {to_str(key)}: {to_str(tree[key]['value'])}")
    return res

def get_result_stylish_formatt(tree):
    return '{' + '\n' + '\n'.join(get_stylish_formatt(tree))+ '\n' + '}'
