# 745. Prefix and Suffix Search
# Hard

# 1093

# 333

# Add to List

# Share
# Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

# Example 1:

# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]

# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

# Constraints:

# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.


# This solution works:


class WordFilter:

    def __init__(self, words: List[str]):
        self.dict = {}
        
        '''
        memoizing all the combinations and update it with later index
        '''
        for idx, word in enumerate(words):
            N = len(word)
            for i in range(1, N+1):
                for j in range(1, N+1):
                    self.dict[(word[:i], word[-j:])] = idx

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.dict:
            return self.dict[(prefix, suffix)]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)