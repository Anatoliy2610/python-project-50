import json


def generate_diff(file1_path, file2_path):
    first_file_value = json.load(open(file1_path))
    second_file_value = json.load(open(file2_path))
    keys_first_file = sorted(list(first_file_value))
    keys_second_file = sorted(list(second_file_value))
    result = []
    for item in keys_first_file:
        if item in keys_second_file:
            if first_file_value[item] == second_file_value [item]:
                result.append('  ' + str(item) + ': ' + str(first_file_value[item]))
            else:
                result.append('- ' + str(item) + ': ' + str(first_file_value[item]))
                result.append('+ ' + str(item) + ': ' + str(second_file_value[item]))
        else:
            result.append('- ' + str(item) +': ' + str(first_file_value[item]))

    for item2 in keys_second_file:
        if item2 not in keys_first_file:
            result.append('+ ' + str(item2) + ': ' + str(second_file_value[item2]))
    result = '\n'.join(result)

