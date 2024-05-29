def walk_to_tree(tree, depth=1, symbol='  ', res=[]):
    for key in tree:
        if type(tree[key]) is dict:
            res.append(f'{symbol*depth}{str(key).lower()}: ' + '{')
            walk_to_tree(tree[key], depth+1)
            res.append(f'{symbol*(depth+1)}' + '}')
        else:
            res.append(f'{symbol*depth}{str(key).lower()}: {str(tree[key]).lower()}')
    return res


def get_stylish_formatt(tree, depth=0, symbol='  ', result=[]):
    for item in tree.values():
        if item.get('children'):
            result.append(f"{symbol*depth}  {str(item.get('name')).lower()}: " + '{')
            get_stylish_formatt(item.get('children'), depth+1)
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
