hex_bin_mappings = {'0': '0000',
                       '1': '0001',
                       '2': '0010',
                       '3': '0011',
                       '4': '0100',
                       '5': '0101',
                       '6': '0110',
                       '7': '0111',
                       '8': '1000',
                       '9': '1001',
                       'A': '1010',
                       'B': '1011',
                       'C': '1100',
                       'D': '1101',
                       'E': '1110',
                       'F': '1111'}

bin_hex_mappings = {v: k for k, v in hex_bin_mappings.items()}

hex_dec_mappings = {'0': 0,
                    '1': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                    '8': 8,
                    '9': 9,
                    'A': 10,
                    'B': 11,
                    'C': 12,
                    'D': 13,
                    'E': 14,
                    'F': 15}


def hex_to_bin(hex_string):
    result = ''
    for c in hex_string:
        if c != '\n':
            result += hex_bin_mappings[c]

    return result


def hex_to_dec(hex_string):
    result = 0
    for i, c in enumerate(hex_string):
        result += hex_dec_mappings[c] * 16 ** (len(hex_string) - i - 1)

    return str(result)


def bin_to_hex(bin_string):
    result = '0x'

    while len(bin_string) % 4 != 0:
        bin_string = '0' + bin_string

    while len(bin_string) != 0:
        result += bin_hex_mappings[bin_string[:4]]
        bin_string = bin_string[4:]

    return result


def bin_to_dec(bin_string):
    result = 0
    for i, c in enumerate(bin_string):
        if c == '1':
            result += 2 ** (len(bin_string) - i - 1)

    return str(result)

