from gendiff.formators.format_stylish import format_stylish


def choose_format(tree, format='stylish'):
    if format == 'stylish':
        return format_stylish(tree)
