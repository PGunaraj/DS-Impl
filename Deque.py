# DEQUE

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def deleteFront(self):
        return self.items.pop()

    def deleteRear(self):
        return self.items.pop(0)

    def printDeque(self):
        print(self.items)


d = Deque()
print(d.isEmpty())
d.addFront(5)
d.addFront(1)
d.addRear("end")
print(d.size())
d.addRear("end+1")
d.printDeque()
d.deleteFront()
d.printDeque()
d.deleteRear()
d.printDeque()
print(d.size())