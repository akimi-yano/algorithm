# 1405. Longest Happy String
# Medium

# 329

# 73

# Add to List

# Share
# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

# Given three integers a, b and c, return any string s, which satisfies following conditions:

# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
# If there is no such string s return the empty string "".

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
# Example 3:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
 

# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0



# THIS APPROACH DOES NOT WORK :

# import heapq
# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         '''
#         keep track of the previous character 3 in a row -> break loop/return 
#         keep track of countes
        
#         '''
#         ans = ""
#         maxheap = []
        
#         if a>0:
#             heapq.heappush(maxheap,(a*(-1),'a'))
#         if b>0:
#             heapq.heappush(maxheap,(b*(-1),'b'))
#         if c>0:
#             heapq.heappush(maxheap,(c*(-1),'c'))
        
#         while maxheap:

#             count, char = heapq.heappop(maxheap)
#             count *= (-1)
#             if count > 0:
#                 if prev != char:
#                     ans += char
#                     count -= 1
#             else:
#                 continue
#             if count > 0:
#                 ans += char
#                 count -= 1
#                 temp.append(count*(-1), char)
#             else:            
#                 continue
#             prev = char
#         return ans 
                
                
# THIS APPROACH WORKS !!!:

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {'a': a, 'b': b, 'c': c}
        keys = list(counts.keys())
        for key in keys:
            if counts[key] == 0:
                del counts[key]
        # last = last character used; repeated = boolean if the last
        # character was already used twice.
        def helper(last, repeated):
            # find all the remaining character/count tuples
            kvs = counts.items()
            # if we repeated the last character already, we
            # should filter that one out.
            if repeated:
                kvs = [kv for kv in counts.items() if kv[0] != last ]
            # if there are no more characters to process, return
            if len(kvs) < 1:
                return ''
            
            # choose the most frequent letter; it shoud be used first.
            k, v = max(kvs, key=lambda kv: kv[1])
            will_repeat = False
            # if the chosen letter was already used last time, set
            # the repeat boolean to True
            if k == last:
                will_repeat = True
            counts[k] -= 1
            # if the count goes to zero, delete from the counts dict.
            if counts[k] < 1:
                del counts[k]
            # return the current letter plus the result from the 
            # recursive call.
            return k + helper(k, will_repeat)
        
        return helper(None, False)