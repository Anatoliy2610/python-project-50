def get_parsing(arr1, arr2):
    keys_first_file = sorted(list(arr1))
    keys_second_file = sorted(list(arr2))
    result = []
    for item in keys_first_file:
        if item in keys_second_file:
            if arr1[item] == arr2 [item]:
                result.append('  ' + str(item) + ': ' + str(arr1[item]))
            else:
                result.append('- ' + str(item) + ': ' + str(arr1[item]))
                result.append('+ ' + str(item) + ': ' + str(arr2[item]))
        else:
            result.append('- ' + str(item) +': ' + str(arr1[item]))

    for item2 in keys_second_file:
        if item2 not in keys_first_file:
            result.append('+ ' + str(item2) + ': ' + str(arr2[item2]))
    return result