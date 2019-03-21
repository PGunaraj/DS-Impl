class Node:
	def __init__(self,val):
		self.data=val
		self.next=None
		
class LL:
	def __init__(self):
		self.head=None
	
	#add the node at end each time
	def add(self,val):
		new=Node(val)
		if self.head is None:
			self.head=new
		else:
			node=self.head
			while node.next != None:
				node=node.next
			node.next=new
	
	#delete the node with given value
	def delete(self,val):
		if self.head is None:
			print("LL EMPTY, can't delete")
		elif self.head.data==val:
			self.head=self.head.next
		else:
			prev=self.head
			node=prev.next
			while node is not None and node.data!=val:
				node=node.next
			if node is None:
				print("Error!Not Found")
			else:
				prev.next=node.next
	
	def display(self):
		if self.head is None:
			print("LL EMPTY")
		node=self.head
		while node != None:
			print(node.data,end=" ")
			node=node.next
	
	def size(self):
		l=0
		if self.head is None:
			print(l)
		else:
			l+=1
			node=self.head
			while node.next != None:
				l+=1
				node=node.next
			print(l)

l=LL()
l.add(1)
l.add(2)
l.add(3)
l.display()
l.size()
l.delete(2)
l.display()
l.delete(5)
l.delete(3)
l.display()
l.size()
l.delete(1)
l.display()
l.size()


#AddAtFront
def addAtFront(self,val):
		new =Node(val)
		if self.head is None:
			self.head=new
		else:
			new.next=self.head
			self.head=new


#AddAfterGivenNode
def addAfterNode(self,val,x):
		new=Node(val)
		if x==0:
			if self.head is None:
				self.head=new
			else:
				new.next=self.head
				self.head=new
		elif x is None:
			print("ERROR!specify node value. CAN'T INSERT",val)
		else:
			prev=self.head
			while prev is not None and prev.data!=x:
				prev=prev.next
			if prev is not None and prev.data==x:
				new.next=prev.next
				prev.next=new
			else:
				print("ERROR!node not found. CAN'T INSERT",val)



class Node:
    def __init__(self, inidata):
        self.data = inidata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class unorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


ll = unorderedList()
ll.add(6)
ll.add(5)
print(ll.search(5))
ll.add(4)
print(ll.size())
ll.remove(5)
print(ll.size())
print(ll.search(5))
ll.printList()
