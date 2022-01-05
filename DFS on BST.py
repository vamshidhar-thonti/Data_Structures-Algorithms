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

    '''
        Pre-Order  : Gets all the values in a sorted order, starts from the left most leaf.
                     [32, 74, 86, 100, 111, 120, 150]
        In-Order   : Gets all the values such that re-construction of the tree is possible.
                     [100, 74, 32, 86, 120, 111, 150]
        Post-Order : Gets all the leafs from the left first, then parent node, then leaves to the right.
                     [32, 86, 74, 111, 150, 120, 100]
    '''

    def DFS_pre_order(self):
        def _traverse_pre_order(node, pre_order_list):
            if node.left is not None:
                _traverse_pre_order(node.left, pre_order_list)
            pre_order_list.append(node.value)
            if node.right is not None:
                _traverse_pre_order(node.right, pre_order_list)
            return pre_order_list
        return _traverse_pre_order(self.root, [])

    def DFS_in_order(self):
        def _traverse_in_order(node, in_order_list):
            in_order_list.append(node.value)
            if node.left is not None:
                _traverse_in_order(node.left, in_order_list)
            if node.right is not None:
                _traverse_in_order(node.right, in_order_list)
            return in_order_list
        return _traverse_in_order(self.root, [])

    def DFS_post_order(self):
        def _traverse_post_order(node, post_order_list):
            if node.left is not None:
                _traverse_post_order(node.left, post_order_list)
            if node.right is not None:
                _traverse_post_order(node.right, post_order_list)
            post_order_list.append(node.value)
            return post_order_list
        return _traverse_post_order(self.root, [])        

# Tree Structure:

#         __100__
#        /        \
#     74           120
#    /  \         /   \
#  32    86    111     150



bst = BinarySearchTree()
bst.insert(100)
bst.insert(74)
bst.insert(32)
bst.insert(120)
bst.insert(86)
bst.insert(111)
bst.insert(150)

print(bst.DFS_pre_order())
print(bst.DFS_in_order())
print(bst.DFS_post_order())

# print(json.dumps(traverse(bst.root), indent=4, sort_keys=True))
