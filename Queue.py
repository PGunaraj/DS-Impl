# QUEUE
#using Array with extra size parameter
class Queue:
	def __init__(self,size):
		self.size=size
		self.front=self.len=0
		self.rear=-1
		self.queue=[None]*size
	def enqueue(self,v):
		if (self.len==self.size):
			print("Q FULL, can't insert")
		else:
			self.rear=(self.rear+1)%self.size
			self.queue[self.rear]=v
			self.len+=1
	def dequeue(self):
		if self.len==0:
			print("Q EMPTY,can't delete")
		else:
			self.front=(self.front+1)%self.size
			self.len-=1
	def display(self):
		print("len",self.len)
		if self.len==0:
			print("Q EMPTY")
		elif self.rear>self.front:
			for i in range(self.front,self.rear+1):
				print(self.queue[i],end=" ")
			print()
		else:
			for i in range(self.front,self.size):
				print(self.queue[i],end=" ")
			for i in range(self.rear+1):
				print(self.queue[i],end=" ")
			print()

q=Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.dequeue()
q.dequeue()
q.enqueue(5)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()


#using Array without extra size parameter
class Queue:
	def __init__(self,size):
		self.size=size
		self.front=0
		self.rear=-1
		self.queue=[None]*size
	def enqueue(self,v):
		if (((self.rear+1)%self.size==self.front) and self.rear!=-1):
			print("Q FULL, can't insert")
		else:
			self.rear=(self.rear+1)%self.size
			self.queue[self.rear]=v
	def dequeue(self):
		if self.rear==-1:
			print("Q EMPTY,can't delete")
		elif self.front==self.rear:
			self.front=0
			self.rear=-1
		else:
			self.front=(self.front+1)%self.size
	def len(self):
		if self.rear==-1:
			print("Q EMPTY")
		elif self.rear>self.front:
			print("len",self.rear-self.front+1)
		else:
			print("len",(self.size-self.front)+self.rear+1)
	def display(self):
		if self.rear==-1:
			print("Q EMPTY")
		elif self.rear>self.front:
			for i in range(self.front,self.rear+1):
				print(self.queue[i],end=" ")
			print()
		else:
			for i in range(self.front,self.size):
				print(self.queue[i],end=" ")
			for i in range(self.rear+1):
				print(self.queue[i],end=" ")
			print()

q=Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.len()
q.display()
q.dequeue()
q.dequeue()
q.enqueue(5)
q.len()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()

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
