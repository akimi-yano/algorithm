# 1032. Stream of Characters

# Implement the StreamChecker class as follows:

# StreamChecker(words): Constructor, init the data structure with the given words.
# query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.


# Example:

# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the wordlist


# Note:

# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.




# THIS SOLUTION WORKS !!!!!!! I LOVE THIS PROBLEM !!!
# I used reversed TRIE - maybe there is a better soltion though !


class Node:
    def __init__(self):
        self.prev = {}
        self.is_beginning = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.history = []        
        self.root = Node()
        for word in words:
            cur = self.root
            for char in reversed(word):
                if char not in cur.prev:
                    cur.prev[char] = Node()
                cur = cur.prev[char]  
            cur.is_beginning = True
            

    def query(self, letter: str) -> bool:
        cur = self.root
        self.history.append(letter)
        temp = []
        while self.history:
            popped = self.history.pop()
            temp.append(popped)
            if popped in cur.prev:
                if cur.prev[popped].is_beginning == True:
                    self.history.extend(reversed(temp))
                    return True
                cur = cur.prev[popped]
            else:
                self.history.extend(reversed(temp))
                return False
        self.history.extend(reversed(temp))
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)



# Optimization ! for the solution above that works !
# Used for loop instead of (while loop and pop and append them back)

class Node:
    def __init__(self):
        self.prev = {}
        self.is_beginning = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.history = []        
        self.root = Node()
        for word in words:
            cur = self.root
            for char in reversed(word):
                if char not in cur.prev:
                    cur.prev[char] = Node()
                cur = cur.prev[char]  
            cur.is_beginning = True
            

    def query(self, letter: str) -> bool:
        cur = self.root
        self.history.append(letter)
        for c in reversed(self.history):
            if c in cur.prev:
                if cur.prev[c].is_beginning == True:
                    return True
                cur = cur.prev[c]
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)