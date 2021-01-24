# 1737. Change Minimum Characters to Satisfy One of Three Conditions
# Medium

# 67

# 134

# Add to List

# Share
# You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

# Your goal is to satisfy one of the following three conditions:

# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
# Return the minimum number of operations needed to achieve your goal.

 

# Example 1:

# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
# Example 2:

# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to "eee".
 

# Constraints:

# 1 <= a.length, b.length <= 105
# a and b consist only of lowercase letters.

# This solution works:
from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # char -> only 26 lowercase so its ok to do time complexity of O(N^2)
        '''
        a "aba", b = "caa"
        
        aab aac
        
        1 greatest a = b
        b->a
        bbb
        
        aa-> c 2
        
        2 greatest b = c
        
        3 2 operations to change to a
        
        b and c
        find the most frequent counts
        '''
        acount = Counter(a)
        bcount = Counter(b)
        ccount = acount + bcount
        most_frequent = max(ccount.values())
        opt3num = len(a)+len(b) - most_frequent
        
        alist = list(acount.items())
        blist = list(bcount.items())
        alist.sort()
        blist.sort()
        
        # Option 1: make "a" smaller than "b"
        opt1num = float('inf')
        b_changed = 0
        # every loop, keep everything in blist from "letter" and above.
        for b_letter, b_count in blist:
            # edge case: if the letter "a" was in blist, there is no way to change letters in alist to be smaller than blist
            if b_letter == "a":
                b_changed += b_count
                continue
            a_changed = 0
            for a_letter, a_count in reversed(alist):
                if b_letter > a_letter:
                    break
                a_changed += a_count
            opt1num = min(opt1num, b_changed + a_changed)
            b_changed += b_count
        if alist[-1][0] == "z":
            b_changed += alist[-1][1]
        opt1num = min(opt1num, b_changed)
        
        # Option 2: make "a" bigger than "b"
        opt2num = float('inf')
        a_changed = 0
        # every loop, keep everything in alist from "letter" and above.
        for a_letter, a_count in alist:
            # edge case: if the letter "a" was in alist, there is no way to change letters in blist to be smaller than alist
            if a_letter == "a":
                a_changed += a_count
                continue
            b_changed = 0
            for b_letter, b_count in reversed(blist):
                if a_letter > b_letter:
                    break
                b_changed += b_count
            opt2num = min(opt2num, a_changed + b_changed)
            a_changed += a_count
        if blist[-1][0] == "z":
            a_changed += blist[-1][1]
        opt2num = min(opt2num, a_changed)
        
        return min(opt1num, opt2num, opt3num)


# This approach does not work:
# from collections import Counter
# class Solution:
#     def minCharacters(self, a: str, b: str) -> int:
#         '''
#         a "aba", b = "caa"
        
#         aab aac
        
#         1 greatest a = b
#         b->a
#         bbb
        
#         aa-> c 2
        
#         2 greatest b = c
        
#         3 2 operations to change to a
        
#         b and c
#         find the most frequent counts
#         '''
#         acount = Counter(a)
#         bcount = Counter(b)
#         ccount = acount + bcount
#         most_frequent = max(ccount.items(), key = lambda x: x[1])[1]
#         opt3num = len(a)+len(b) - most_frequent
        
#         opt1num = 0
#         greatesta = max(a)
#         for elem in b:
#             if elem <= greatesta:
#                 opt1num += 1
                
#         opt2num = 0
#         greatestb = max(b)
#         for elem in a:
#             if elem <= greatestb:
#                 opt2num += 1
#         return min(opt1num, opt2num, opt3num)