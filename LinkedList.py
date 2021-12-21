class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
    
    def print_all(self):
        begin = self.head
        linkedListArray = []
        while begin is not None:
            linkedListArray.append(begin.value)
            begin = begin.next
        print(linkedListArray)

    def insert(self, index, value):
        newNode = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            try:
                leader = self.traverseToIndex(index - 1)
                newNode.next = leader.next
                leader.next = newNode
                self.length += 1
            except Exception:
                print('Check the index of your insert!')
    
    def remove(self, index):
        if index == 0:
            self.head = self.traverseToIndex(index + 1)
        elif index == self.length - 1:
            leader = self.traverseToIndex(index - 1)
            leader.next = None
            self.tail = leader
        else:
            leader = self.traverseToIndex(index - 1)
            current = self.traverseToIndex(index)
            leader.next = current.next
        self.length -= 1

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first.next
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

list1 = LinkedList(10)
list1.append(5)
list1.append(16)
list1.prepend(1)
list1.insert(2, 99)
list1.insert(0, 12)
list1.insert(6, 12)
list1.insert(5, 1000)
list1.print_all()
list1.remove(7)
list1.print_all()
list1.remove(0)
list1.print_all()
list1.remove(4)
list1.print_all() 
list1.reverse()
list1.print_all() 
print(list1.length)