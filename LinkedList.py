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