import sys, json

def traverse(node):
  tree = { 'value': node.value }
  tree['left'] = None if node.left == None else traverse(node.left)
  tree['right'] = None if node.right == None else traverse(node.right)
  return tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        isPositionFound = False
        start = self.root
        if self.root == None:
            self.root = newNode
        else:
            while not isPositionFound:
                if value > start.value:
                    if start.right == None:
                        start.right = newNode
                        isPositionFound = True
                    else:
                        start = start.right
                elif value < start.value:
                    if start.left == None:
                        start.left = newNode
                        isPositionFound = True
                    else:
                        start = start.left
                else:
                    sys.exit("value should be either > or <")


    def lookup(self, value):
        start = self.root
        while start is not None:
            if value == start.value:
                return start
            elif value < start.value:
                start = start.left
            else:
                start = start.right
        
        return False

    def remove(self, value):
        pass
        # Need to work on it

bst = BinarySearchTree()
bst.insert(100)
bst.insert(74)
bst.insert(120)
bst.insert(32)
bst.insert(86)
bst.insert(111)
bst.insert(150)
print(vars(bst.lookup(150)))
print(vars(bst.lookup(100)))
print(vars(bst.lookup(32)))
print(vars(bst.lookup(74)))
print(vars(bst.lookup(86)))
print(vars(bst.lookup(111)))
print(vars(bst.lookup(120)))
print(vars(bst.lookup(1)))

# print(json.dumps(traverse(bst.root), indent=4, sort_keys=True))
