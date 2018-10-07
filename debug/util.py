def list_to_string(target_list, coupler):
    result = ''

    for target in target_list:
        result += target + coupler

    return result


def hexencode_to_string(target_hex_encode):
    result = ''

    for i in range(2, len(target_hex_encode), 2):
        result += chr(int(target_hex_encode[i:i+2], 16))

    return result


def hex_decode(hex_string):
    if hex_string.startswith('0x'):
        return hex_string[2:]
    else:
        return hex_string


def split_by_length(string, length):
    string_length = len(string)

    result = []
    for i in range(0, string_length, length):
        result.append(string[i:i+length])

    return result
