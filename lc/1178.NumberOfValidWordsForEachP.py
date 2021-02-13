# 1178. Number of Valid Words for Each Puzzle
# Hard

# 260

# 32

# Add to List

# Share
# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].


# Example :

# Input: 
# words = ["aaaa","asas","able","ability","actt","actor","access"], 
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa" 
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.


# Constraints:

# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] are English lowercase letters.
# Each puzzles[i] doesn't contain repeated characters.




# This solution works:




class TreeNode:
    def __init__(self, char=None):
        self.count = 0
        self.char = char
        self.left = None
        self.right = None

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        '''
        make a tree out of words 
        left is when we have it
        right is when we dont have it
        
        words = ["aaaa","asas","able","ability","actt","actor","access"], 
        wordsset = {a},{as},{able},{abilty},{act},{actor},{aces}
        a1
        /\
    b
    /\s1
        
        puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
        '''
        def helper(cur, foundfirst, firstchar, puzzleset):
            if not cur:
                return 0
            if not cur.char and foundfirst:
                return cur.count
            total = 0
            char = cur.char
            if char == firstchar:
                foundfirst = True
            if char in puzzleset:
                total += helper(cur.left, foundfirst, firstchar, puzzleset)
                if char != firstchar:
                    total += helper(cur.right, foundfirst, firstchar, puzzleset)
            else:
                total += helper(cur.right, foundfirst, firstchar, puzzleset)
            return total
        
        # made tree
        root = TreeNode()
        for word in words:
            wordset = set(word)
            cur = root
            for char in "abcdefghijklmnopqrstuvwxyz":
                if cur.char is None:
                    cur.char = char
                if char in wordset:
                    if cur.left is None:
                        cur.left = TreeNode()
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = TreeNode()
                    cur = cur.right
            cur.count +=1
        
        ans = []
        # traverse the tree
        for puzzle in puzzles:
            firstchar = puzzle[0]
            puzzleset = set(puzzle)
            cur = root
            ans.append(helper(root, False, firstchar, puzzleset))
        return ans
        
        
        
        