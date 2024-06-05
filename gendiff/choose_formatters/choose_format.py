from gendiff.choose_formatters.stylish_format import get_result_stylish_format
from gendiff.choose_formatters.plain_format import get_result_plain_format
from gendiff.choose_formatters.json_format import get_json_format


def choose_format(tree, format='stylish'):
    if format == 'stylish':
        return get_result_stylish_format(tree)
    if format == 'plain':
        return get_result_plain_format(tree)
    if format == 'json':
        return get_json_format(tree)
    else:
        return 'Выбран неверный формат'
