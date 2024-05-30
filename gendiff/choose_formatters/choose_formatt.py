from gendiff.choose_formatters.stylish_formatt import get_result_stylish_formatt
from gendiff.choose_formatters.plain_formatt import get_result_plain_formatt
from gendiff.choose_formatters.json_format import get_json_format


def choose_formatt(tree, format='stylish'):
    if format == 'stylish':
        return get_result_stylish_formatt(tree)
    if format == 'plain':
        return get_result_plain_formatt(tree)
    if format == 'json':
        return get_json_format(tree)
    else:
        return 'Выбран неверный формат'
