from gendiff.choose_formatters.stylish_formatt import get_stylish_formatt


def choose_formatt(tree, format='stylish'):
    if format == 'stylish':
        return get_stylish_formatt(tree)
