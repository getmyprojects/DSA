"""
input: aaaabbccc
output: 4a2b3c

input: aaaabbccca
output: 4a2b3c1a
"""


def string_encode(input_str):
    if len(input_str) == 0:
        return ''
    counter = 0
    prev = input_str[0]
    res = ''

    for i in range(len(input_str)):
        #print(prev, c)
        if input_str[i] == prev:
            counter += 1
        else:
            res += str(counter)+prev
            counter = 1
        prev = input_str[i]
        if i == len(input_str)-1:
            res += str(counter)+prev

    return res


if __name__ == '__main__':
    res = string_encode('aaaabbccc')
    print(res)
    # ===
    print(string_encode('aaaabbccca'))
    # ===
    print(string_encode('abcd'))