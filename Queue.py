# QUEUE

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
