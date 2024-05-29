def walk_to_tree(tree, depth=1, symbol='  ', res=[]):
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{symbol*depth}{str(key).lower()}: ' + '{')
            walk_to_tree(tree[key], depth+1)
            res.append(f'{symbol*(depth+1)}' + '}')
        else:
            res.append(f'{symbol*depth}{str(key).lower()}: {str(tree[key]).lower()}')
    return res


def formatt_stylish(tree, depth=0, symbol='  ', result=[]):
    for item in tree.values():
        if item.get('children'):
            result.append(f"{symbol*depth}  {str(item.get('name')).lower()}: " + '{')
            format_stylish(item.get('children'), depth+1)
            result.append(f"{symbol*depth}" + '}')
        elif type(item.get('old_value')) is dict:
            result.append(f"{symbol*depth}- {str(item.get('name')).lower()}: " + '{')
            result.extend(walk_to_tree(item.get('old_value'), depth+1))
            result.append(f"{symbol*(depth+1)}" + '}')
        elif type(item.get('new_value')) is dict:
            result.append(f"{symbol*depth}+ {str(item.get('name')).lower()}: " + '{')
            result.extend(walk_to_tree(item.get('new_value'), depth+1))
            result.append(f"{symbol*(depth+1)}" + '}')
        else:
            if item.get('action') == 'deleted':
                result.append(f"{symbol*depth}- {str(item.get('name')).lower()}: {str(item.get('old_value')).lower()}")
            elif item.get('action') == 'added':
                result.append(f"{symbol*depth}+ {str(item.get('name')).lower()}: {str(item.get('new_value')).lower()}")
            elif item.get('action') == 'unchanged':
                result.append(f"{symbol*depth}  {str(item.get('name')).lower()}: {str(item.get('value')).lower()}")
            elif item.get('action') == 'modified':
                result.append(f"{symbol*depth}- {str(item.get('name')).lower()}: {str(item.get('old_value')).lower()}")
                result.append(f"{symbol*depth}+ {str(item.get('name')).lower()}: {str(item.get('new_value')).lower()}")
    return result




# nax = {'common': {'action': 'nested', 'name': 'common', 'children': {'follow': {'action': 'added', 'name': 'follow', 'new_value': False}, 'setting1': {'action': 'unchanged', 'name': 'setting1', 'value': 'Value 1'}, 'setting2': {'action': 'deleted', 'name': 'setting2', 'old_value': 200}, 'setting3': {'action': 'modified', 'name': 'setting3', 'new_value': None, 'old_value': True}, 'setting4': {'action': 'added', 'name': 'setting4', 'new_value': 'blah blah'}, 'setting5': {'action': 'added', 'name': 'setting5', 'new_value': {'key5': 'value5'}}, 'setting6': {'action': 'nested', 'name': 'setting6', 'children': {'doge': {'action': 'nested', 'name': 'doge', 'children': {'wow': {'action': 'modified', 'name': 'wow', 'new_value': 'so much', 'old_value': ''}}}, 'key': {'action': 'unchanged', 'name': 'key', 'value': 'value'}, 'ops': {'action': 'added', 'name': 'ops', 'new_value': 'vops'}}}}}, 'group1': {'action': 'nested', 'name': 'group1', 'children': {'baz': {'action': 'modified', 'name': 'baz', 'new_value': 'bars', 'old_value': 'bas'}, 'foo': {'action': 'unchanged', 'name': 'foo', 'value': 'bar'}, 'nest': {'action': 'modified', 'name': 'nest', 'new_value': 'str', 'old_value': {'key': 'value'}}}}, 'group2': {'action': 'deleted', 'name': 'group2', 'old_value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'action': 'added', 'name': 'group3', 'new_value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}

# print('{' + '\n' + '\n'.join(format_stylish(nax))+ '\n' + '}')


