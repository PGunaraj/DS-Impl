# QUEUE
#using list
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def printQueue(self):
        print(self.items)


q = Queue()
q.enqueue(1)
q.enqueue("love")
q.enqueue(True)
q.enqueue("India")
print(q.size())
print(q.isEmpty())
q.printQueue()
q.dequeue()
q.dequeue()
print(q.size())
q.printQueue()

#using LL
class Node:
	def __init__(self,v):
		self.data=v
		self.next=None

class Queue:
	def __init__(self):
		self.front=None
		self.rear=None
	def enqueue(self,v):
		temp=Node(v)
		if not self.front:
			self.front=temp
			self.rear=temp
		else:
			self.rear.next=temp
			self.rear=temp
	def dequeue(self):
		if not self.front:
			return
		else:
			temp=self.front
			self.front=self.front.next
		if not self.front:
			self.rear=None
		return temp
	def printQueue(self):
		temp=self.front
		while temp:
			print(temp.data,end=" ")
			temp=temp.next
		print()
	def top(self):
		return self.front.data

q=Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(1)
q.printQueue()
q.dequeue()
print(q.top())
