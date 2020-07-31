# Word Break II
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


# initial plan:
        # iterrate dict 
        # check with word length
        # keep tract of words in string with space
        # pass in the rest in recusion 
        # when all words done 
        # append


# this solution passed 31 / 36 test cases passed.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        res = []
        def helper(s,ans):
            if len(s)<1:
                res.append(ans)
                return         
            for word in wordDict:
                if s[:len(word)]==word:
                    helper(s[len(word):],ans+' '+word)
            
        for word in wordDict:
                if s[:len(word)]==word:
                    helper(s[len(word):],word)
        return res
    

# but then I got a test case like this:

# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# changing strategy now ....


# this solution works

# def wordBreak(self, s, wordDict):
#     """
#     :type s: str
#     :type wordDict: Set[str]
#     :rtype: List[str]
#     """
#     return self.helper(s, wordDict, {})
    
# def helper(self, s, wordDict, memo):
#     if s in memo: return memo[s]
#     if not s: return []
    
#     res = []
#     for word in wordDict:
#         if not s.startswith(word):
#             continue
#         if len(word) == len(s):
#             res.append(word)
#         else:
#             resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
#             for item in resultOfTheRest:
#                 item = word + ' ' + item
#                 res.append(item)
#     memo[s] = res
#     return res


# this works!!!!!! most intuitive to me 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        memo={}
        
        # input: string without spaces
        # output: list of sentences with spaces placed
        # ex.
        # in:  "applepenapple"
        # out ["apple pen apple", "applepen apple"]
        def helper(s):
            if s in memo:
                return memo[s]
            if len(s)<1:
                return ['']
            res = []
            for word in words:
                if len(word)<=len(s) and word==s[:len(word)]:
                    # print(s, word, ',', helper(s[len(word):]))
                    sentences = helper(s[len(word):])
                    for sentence in sentences:
                        if sentence == '':
                            res.append(word)
                        else:
                            res.append(word + ' ' + sentence)
            memo[s]=res
            return res
        return helper(s)  