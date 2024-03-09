from stack import Stack


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    binary = ""
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    while not s.is_empty():
        binary += str(s.pop())
    return binary


print(int(convert_int_to_bin(242), 2))
