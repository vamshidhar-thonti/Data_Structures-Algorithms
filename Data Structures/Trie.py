class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.children = {}
        self.end_here = False

class Trie:

    def __init__(self) -> None:
        self.root = Node(None)

    def insert(self, word):
        parent = self.root
        for index, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = Node(word[:index + 1])
            parent = parent.children[char]
            if index == len(word) - 1:
                parent.end_here = True

    def search(self, word):
        parent = self.root
        for char in word:
            if char not in parent.children.keys():
                return False
            parent = parent.children[char]
        return parent.end_here

    def starts_with(self, sub_word):
        parent = self.root
        for char in sub_word:
            if char not in parent.children.keys():
                return False
            parent = parent.children[char]
        return True

    def delete(self, word):
        '''
            Doesn't delete the sub nodes if no children.
            It will just set the end_here value to False (only if that value is already inserted),
            so that it doesn't be found where search method is called.
            But if starts_with method is called, it returns True.
        '''
        parent = self.root
        for char in word:
            if char not in parent.children.keys():
                return "No such word exist"
            if char in parent.children.keys():
                parent = parent.children[char]
                if parent.end_here:
                    parent.end_here = False
                    return f"Deleted {word}"

    # def words_with(self, word):
    #     parent = self.root
    #     for char in word:
    #         if char not in parent.children.keys():
    #             return "No such word exist"
    #         else:
    #             parent = parent.children[char]
    #     prefix = word
    #     visited_nodes = {x:False for x in parent.children.keys()}
    #     def _possibilities(root, words_list):
            
    #         return words_list
    #     return _possibilities(parent, [])

trie = Trie()

trie.insert('apple')
trie.insert('apples')
trie.insert('approx')
trie.insert('bad')
trie.insert('ban')
trie.insert('bank')
trie.insert('band')

# print(trie.search('apple'))
# print(trie.search('apples'))
# print(trie.starts_with('app'))

print(trie.search('bad'))
print(trie.search('ban'))
# print(trie.search('bank'))
# print(trie.search('band'))

# print(trie.delete('ban'))
# print(trie.search('bad'))
# print(trie.search('ban'))
# print(trie.search('bank'))
# print(trie.search('band'))

# print(trie.starts_with('ban'))