from gendiff.formatters.stylish_formatt import formatt_stylish


def choose_formatt(tree, format='stylish'):
    if format == 'stylish':
        return formatt_stylish(tree)
