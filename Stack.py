class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def print_all(self):
        bottom = self.bottom
        stack_list = []
        while bottom is not None:
            stack_list.append(bottom.value)
            bottom = bottom.next
        print(stack_list)

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.bottom = newNode
            self.top = self.bottom
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1
    
    def peek(self):
        return self.top.value
    
    def pop(self):
        if self.length > 0:
            if self.top == self.bottom:
                self.bottom = None
            holdingPointer = self.top            
            self.top = self.top.next
            self.length -= 1
            return holdingPointer.value
        else:
            return None


# s1 = Stack()
# s1.print_all()
# s1.push('Google')
# s1.push('FB')
# s1.push('Udemy')
# s1.print_all()
# print(s1.pop(), s1.length)

class StackWArray:
    def __init__(self):
        self.array = []
        self.bottom = None
        self.top = self.bottom
        self.length = 0

    def push(self, value):
        self.array.append(value)
        if self.length == 0:
            self.bottom = 0
        self.length += 1
        self.top = self.length - 1
        return self.array

    def pop(self):
        if self.length > 0:
            peek_value = self.array[-1]
            del self.array[-1]
            self.length -= 1
            self.top = self.length - 1
            return peek_value
        else:
            print('No more values')
            return None
    
    def peek(self):
        return self.array[self.top]


s2 = StackWArray()
print(s2.array)
s2.push(1)
s2.push(144)
s2.push(12)
print(s2.array, s2.length)
s2.pop()
s2.pop()
print(s2.array)
print('peek', s2.peek())
print(s2.length)
s2.pop()
print(s2.length)
s2.pop()
