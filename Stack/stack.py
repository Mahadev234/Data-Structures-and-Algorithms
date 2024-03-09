class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# myStack = Stack()
# myStack.push("A")
# myStack.push("B")
# myStack.push("C")
# myStack.push("D")
# print(myStack.is_empty())
# print(myStack.peek())
# print(myStack.get_stack())
# print(myStack.pop())
# print(myStack.get_stack())
