def walk_to_one_dict(dictionary, symbol='  ', depth1=0):
    res = []
    for item in dictionary:
        if type(dictionary[item]) is not dict:
            res.append(f'  {symbol*depth1}{item}: {dictionary[item]}')
        else:
            res.append(f'  {symbol*depth1}{item}' + ': {')
            res.extend(walk_to_one_dict(dictionary[item], '  ', depth1+1))
            res.append(f'{symbol*(depth1)}'+ '}')
    return res


def get_parsing(dict1, dict2):

    def walk_to_two_dicts(dict1, dict2, symbol='  ', depth=1, res=[]):
        keys = set(dict1) | set(dict2)
        for key in sorted(keys):
            if key in dict1 and key in dict2:
                if type(dict1[key]) is not dict and type(dict2[key]) is not dict:
                    if dict1[key] == dict2[key]:
                        res.append(f'{symbol*depth}  {key}: {dict1[key]}')
                    else:
                        res.append(f'{symbol*depth}- {key}: {dict1[key]}')
                        res.append(f'{symbol*depth}+ {key}: {dict2[key]}')
                else:
                    if type(dict1[key]) is dict and type(dict2[key]) is dict:
                        res.append(f'{symbol*depth}  {key}: ' + '{')
                        walk_to_two_dicts(dict1[key], dict2[key], '  ', depth+1)
                        res.append(f'{symbol*(depth)}' + '}')
                    else:
                        if type(dict1[key]) is dict:
                            res.append(f'{symbol*depth}- {key}: ' + '{')
                            res.extend(walk_to_one_dict(dict1[key], '  ', depth+1))
                            res.append(f'{symbol*(depth)}' + '}')
                            res.append(f'{symbol*depth}+ {key}: {dict2[key]}')
                        if type(dict1[key]) is not dict and type(dict2[key]) is dict:
                            res.append(f'{symbol*depth}- {key}: {dict1[key]}')
                            res.append(f'{symbol*depth}+ {key}: ' + '{')
                            walk_to_one_dict(dict2[key], '  ', depth+1)
                            res.append(f'{symbol*(depth)}' + '}')
            if key in dict1 and key not in dict2:
                if type(dict1[key]) is dict:
                    res.append(f'{symbol*depth}- {key}: ' + '{')
                    res.extend(walk_to_one_dict(dict1[key], '  ', depth+1))
                    res.append(f'{symbol*(depth)}' + '}')
                else:
                    res.append(f'{symbol*depth}- {key}: {dict1[key]}')
            if key in dict2 and key not in dict1:
                if type(dict2[key]) is dict:
                    res.append(f'{symbol*depth}+ {key}: ' + '{')
                    res.extend(walk_to_one_dict(dict2[key], '  ', depth+1))
                    res.append(f'{symbol*(depth)}' + '}')
                else:
                    res.append(f'{symbol*depth}+ {key}: {dict2[key]}')

        return res
    return walk_to_two_dicts(dict1, dict2)
