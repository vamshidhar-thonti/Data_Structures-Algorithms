class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.first.value
        return None

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
    
    def dequeue(self):
        if self.length > 0:
            holdingPointer = self.first
            self.first = holdingPointer.next
            self.length -= 1
            return holdingPointer.value
        else:
            self.last = None
        
    
    def print_all(self):
        queue_list = []
        start = self.first
        while start is not None:
            queue_list.append(start.value)
            start = start.next
        print(queue_list)

q1 = Queue()
q1.enqueue(1)
q1.enqueue(5)
q1.enqueue(2)
q1.print_all()
print(q1.peek(), q1.length)
print(q1.dequeue())
print(q1.dequeue())
q1.print_all()
print(q1.dequeue(), q1.length)
q1.print_all()
