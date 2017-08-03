# Ordered List

class Node:
    def __init__(self, item):
        self.items = item
        self.next = None

    def getData(self):
        return self.items

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.items = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count = count + 1
        return count

    def search(self, item):
        current = self.head
        prev = None
        stop = False
        found = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        prev = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                prev = current
                current = current.getNext()
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.next


ol = OrderedList()
ol.add(5)
ol.add(2)
ol.add(7)
ol.add(0)
ol.printList()
print(ol.search(5))
print(ol.size())