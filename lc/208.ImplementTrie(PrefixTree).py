# 208. Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.




# THIS DOES NOT WORK --- 

# class TrieNode:
#     def __init__(self,val):
#         self.val = val
#         self.endhere = False
#         self.next = {}
        
# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root=TrieNode(None)       

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         next_node = self.root
#         for c in word:
#             if c not in next_node.next:
#                 next_node.next[c]=TrieNode(c)
#             next_node=next_node.next
#         next_node.endhere = True
        

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         next_node = self.root
#         for c in word:
#             if c not in next_node.next:
#                 return False
#             next_node=next_node.next
#         if next_node.endhere == True:
#             return True

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
    


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)





# THIS SOLUTION WORKS 


class TrieNode:
# Initialize your data structure here.
def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.is_word = False

class Trie:
def __init__(self):
    self.root = TrieNode()

def insert(self, word):
    current = self.root
    for letter in word:
        current = current.children[letter]
    current.is_word = True

def search(self, word):
    current = self.root
    for letter in word:
        current = current.children.get(letter)
        if current is None:
            return False
    return current.is_word

def startsWith(self, prefix):
    current = self.root
    for letter in prefix:
        current = current.children.get(letter)
        if current is None:
            return False
    return True