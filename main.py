import base_conversions as bc

instr_op = {'000000': 'RD  ',
            '000001': 'WR  ',
            '000010': 'ST  ',
            '000011': 'LW  ',
            '000100': 'MOV ',
            '000101': 'ADD ',
            '000110': 'SUB ',
            '000111': 'MUL ',
            '001000': 'DIV ',
            '001001': 'AND ',
            '001010': 'OR  ',
            '001011': 'MOVI',
            '001100': 'ADDI',
            '001101': 'MULI',
            '001110': 'DIVI',
            '001111': 'LDI ',
            '010000': 'SLT ',
            '010001': 'SLTI',
            '010010': 'HLT ',
            '010011': 'NOP ',
            '010100': 'JMP ',
            '010101': 'BEQ ',
            '010110': 'BNE ',
            '010111': 'BEZ ',
            '011000': 'BNZ ',
            '011001': 'BGZ ',
            '011010': 'BLZ '}


def translate_instruction(i):
    result = ''

    if i[:2] == '00':
        result += 'R \t' + instr_op[i[2:8]] + '\t'
        result += 'sreg=' + bc.bin_to_dec(i[8:12]) + '\t'
        result += 'sreg=' + bc.bin_to_dec(i[12:16]) + '\t'
        result += 'dreg=' + bc.bin_to_dec(i[16:20]) + '\t'

    if i[:2] == '01':
        result += 'I \t' + instr_op[i[2:8]] + '\t'
        result += 'breg=' + bc.bin_to_dec(i[8:12]) + '\t'
        result += 'dreg=' + bc.bin_to_dec(i[12:16]) + '\t'
        result += 'addr=' + bc.bin_to_hex(i[16:])

    if i[:2] == '10':
        result += 'J \t' + instr_op[i[2:8]] + '\t'
        result += 'addr=' + bc.bin_to_hex(i[8:])

    if i[:2] == '11':
        result += 'IO\t' + instr_op[i[2:8]] + '\t'
        result += 'reg1=' + bc.bin_to_dec(i[8:12]) + '\t'
        result += 'reg2=' + bc.bin_to_dec(i[12:16]) + '\t'
        result += 'addr=' + bc.bin_to_hex(i[16:])

    return result


file = open("programfile", "r")
heading = ''
addr = 0

for line in file:
    if line[:2] == '//':
        heading = line[3]
        if heading == 'J':
            addr = 0
        print(line, end='')

    if line[:2] == '0x':
        if heading == 'J':
            line = bc.hex_to_bin(line[2:])
            print(hex(addr).upper() + ':\t' + translate_instruction(line))

        if heading == 'D':
            print(hex(addr).upper() + ':\t' + line[:-1] + ' = ' + bc.hex_to_dec(line[2:-1]))

        addr += 4
