"""
Curious
"""


def print_as_binary(num_list, bit_width):
    if bit_width == 8:
        form_str = '0b{:0>8b}'
    else:
        form_str = '0b{:0>18b}'

    for i in range(0, len(num_list)):
        print(form_str.format(num_list[i]), end=' ')
        print('\t')
