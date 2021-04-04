# 1813. Sentence Similarity III
# Medium

# 58

# 11

# Add to List

# Share
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

# Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

# Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

# Example 1:

# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
# Example 2:

# Input: sentence1 = "of", sentence2 = "A lot of words"
# Output: false
# Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
# Example 3:

# Input: sentence1 = "Eating right now", sentence2 = "Eating"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
# Example 4:

# Input: sentence1 = "Luky", sentence2 = "Lucccky"
# Output: false
 

# Constraints:

# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
# The words in sentence1 and sentence2 are separated by a single space.


# This solution works:


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        left = 0
        
        while left < len(s1):
            if s1[left] == s2[left]:
                left += 1
            else:
                break
        # print(s1, s2, left)
        
        right1 = len(s1) - 1
        right2 = len(s2) - 1
        
        while right1 >= 0:
            if s1[right1] == s2[right2]:
                right1 -= 1
                right2 -= 1
            else:
                break
        # print(right1, right2)
        
        return left > right1
    
    

# This approach does not work:

# class Solution:
#     def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
#         s1 = sentence1.split()
#         s2 = sentence2.split()
      
#         if len(s1) == 0:
#             return True
#         if len(s2) == 0:
#             return True
#         elif len(s2) == 1 and s1:
#             if s1[0] == s2[0] or s1[-1] == s2[0]:
#                 return True
#         elif len(s1) == 1 and s2:
#             if s2[0] == s1[0] or s2[-1] == s1[0]:
#                 return True
#         elif s1 == s2:
#             return True
#         else:
#             for firstend in range(1,len(s1)):
#                 for secondstart in range(firstend, len(s1)):
#                     # print("comparing", s2[:len(s1[:firstend])],s1[:firstend])
#                     # print("also comparing", s2[-len(s1[secondstart:]):] ,s1[secondstart:])
#                     if s2[:len(s1[:firstend])] == s1[:firstend] and len(s2[-len(s1[secondstart:]):]) == len(s1[secondstart:]) and s2[-len(s1[secondstart:]):] == s1[secondstart:]:
#                         return True
#             for firstend in range(1,len(s2)):
#                 for secondstart in range(firstend, len(s2)):
#                     # print("comparing", s1[:len(s2[:firstend])],s2[:firstend])
#                     # print("also comparing", s1[-len(s2[secondstart:]):] ,s2[secondstart:])
#                     if s1[:len(s2[:firstend])] == s2[:firstend] and len(s1[-len(s2[secondstart:]):]) == len(s2[secondstart:]) and s1[-len(s2[secondstart:]):] == s2[secondstart:]:
#                         return True
#             return False