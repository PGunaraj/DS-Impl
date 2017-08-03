# STACK

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def printStack(self):
        return self.items


s = Stack()
s.push(4)
s.push(1)
print(s.size())
print(s.peek())
print(s.pop())
print(s.peek())
s.push(2)
s.push(7)
print(s.printStack())

# Reverse a string using stack
x = Stack()
str = "Hello"
rev = ' '
for ch in str:  # to go through string
    x.push(ch)
while not x.isEmpty():  # to go through stack
    rev = rev + x.pop()
print("reversed string is: ", rev)
