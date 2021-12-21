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
        pass

    def remove(self, value):
        pass

bst = BinarySearchTree()
bst.insert(100)
bst.insert(74)
bst.insert(120)
bst.insert(32)
bst.insert(86)
bst.insert(111)
bst.insert(150)

print(json.dumps(traverse(bst.root), indent=4, sort_keys=True))
