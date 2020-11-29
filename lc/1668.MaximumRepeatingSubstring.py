# 1668. Maximum Repeating Substring
# Easy

# 23

# 7

# Add to List

# Share
# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

# Example 1:

# Input: sequence = "ababc", word = "ab"
# Output: 2
# Explanation: "abab" is a substring in "ababc".
# Example 2:

# Input: sequence = "ababc", word = "ba"
# Output: 1
# Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
# Example 3:

# Input: sequence = "ababc", word = "ac"
# Output: 0
# Explanation: "ac" is not a substring in "ababc". 
 

# Constraints:

# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence and word contains only lowercase English letters.

# this approach does not work:

        # count = 0
        # left = 0
        # while left <= len(sequence)-1:
        #     if sequence[left] == word[0] and len(sequence) - left  >= len(word):
                
        #         right = left 
        #         i = 0
        #         while right <= len(sequence)-1 and i <= len(word)-1 and sequence[right] == word[i]:
        #             right += 1
        #             i += 1
        #         if right <= len(sequence)-1 and i <= len(word)-1:
        #             count += 1
        #         left = right + 1
        #     else:
        #         left += 1
        # return count
    

# this approach does not work: 

    # return sequence.count(word)




# this approach does not  work:

    # class Solution:
    # def maxRepeating(self, sequence: str, word: str) -> int:
    #     max_count = 0
    #     left = 0
    #     count = 0
    #     while left <= len(sequence)-1:
    #         if sequence[left] == word[0] and len(sequence) - left  >= len(word):
    #             right = left 
    #             i = 0
    #             while right <= len(sequence)-1 and i <= len(word)-1 and sequence[right] == word[i]:
    #                 right += 1
    #                 i += 1
    #             if i > len(word)-1:
    #                 count += 1
    #             else:
    #                 count = 0 
    #             left = right 
    #         else:
    #             count = 0
    #             left += 1
    #         max_count = max(max_count, count)
    #     return max_count
    
    
# This approach works !!!
    
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        left = 0
        count = 0
        while left <= len(sequence)-1:
            if sequence[left] == word[0] and len(sequence) - left  >= len(word):
                right = left 
                i = 0
                while right <= len(sequence)-1 and i <= len(word)-1 and sequence[right] == word[i]:
                    right += 1
                    i += 1
                if i > len(word)-1:
                    count += 1
                    left = right 
                else:
                    count = 0 
                    left += 1
            else:
                count = 0
                left += 1
            max_count = max(max_count, count)
        return max_count
    
# This solution works ! - much shorter brute force:

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maxrepeat=0
        while maxrepeat*word in sequence: 
            maxrepeat+=1
        return maxrepeat-1