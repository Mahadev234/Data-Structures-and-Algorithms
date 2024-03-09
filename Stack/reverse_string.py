from stack import Stack


def reverse_string(str1):
    for i in range(len(str1)):
        stack.push(str1[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


stack = Stack()
print(reverse_string("vedahaM"))
