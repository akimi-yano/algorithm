# 211. Design Add and Search Words Data Structure
# Medium

# 3877

# 159

# Add to List

# Share
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.


# This solution works:


class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not char in cur.next:
                cur.next[char] = TrieNode()
            cur = cur.next[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        
        def helper(i, cur):
            nonlocal word
            if i > len(word)-1:
                return cur.is_word
            ans = False
            if word[i] in cur.next:
                ans |= helper(i+1, cur.next[word[i]])
            elif word[i] == ".":
                for next_char in cur.next:
                    ans |= helper(i+1, cur.next[next_char])
            return ans
        
        return helper(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)