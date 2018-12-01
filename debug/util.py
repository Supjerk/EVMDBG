def list_to_string(target_list, coupler):
    result = ''

    for target in target_list:
        result += target + coupler

    return result


def list_to_int(target_list):
    result = ''

    for target in target_list:
        result += hex_decode(str(hex(target)))

    result = int(result, 16)

    return result


def hexencode_to_list(target_hex_encode, size):
    string = hex_decode(str(hex(target_hex_encode))).rjust(size * 2, '0')
    result = split_by_length(string, 2)
    
    for i in range(0, len(result)):
        try:
            result[i] = int(result[i], 16)
        except ValueError:
            pass

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
