class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
    
    def print_all(self, reverse=False):
        begin = self.tail if reverse else self.head
        linkedListArray = []
        while begin is not None:
            linkedListArray.append(begin.value)
            begin = begin.prev if reverse else begin.next
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
                follower = leader.next
                leader.next = newNode
                newNode.prev = leader
                newNode.next = follower
                follower.prev = newNode
                self.length += 1
            except Exception:
                print('Check the index of your insert!')
    
    def remove(self, index):
        if index == 0:
            self.head = self.traverseToIndex(index + 1)
            self.head.prev = None
        elif index == self.length - 1:
            leader = self.traverseToIndex(index - 1)
            current = leader.next
            leader.next = None
            current.prev = None
            self.tail = leader
        else:
            leader = self.traverseToIndex(index - 1)
            follower = self.traverseToIndex(index + 1)
            leader.next = follower
            follower.prev = leader
        self.length -= 1

    # def reverse(self):
    #     reverse_list = []
    #     end = self.tail
    #     while end is not None:
    #         reverse_list.append(end.value)
    #         end = end.prev
    #     print(reverse_list)

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
list1.print_all(reverse=True)
print(list1.length)
# list1.reverse()