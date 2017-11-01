# STACK
#using list
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

#using LL
class Node:
	def __init__(self,val):
		self.data=val
		self.next=None

class Stack:
	def __init__(self):
		self.front=None
	def push(self,val):
		newnode=Node(val)
		newnode.next=self.front
		self.front=newnode
	def pop(self):
		temp=self.front
		self.front=self.front.next
		return temp.data
	def top(self):
		return self.front.data
	def isEmpty(self):
		return self.front==None

s=Stack()
s.push(10)
s.push(20)
print(s.pop())
print(s.top())
print(s.isEmpty())
