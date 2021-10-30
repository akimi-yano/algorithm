# 1044. Longest Duplicate Substring
# Hard

# 1178

# 274

# Add to List

# Share
# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

# Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

# Example 1:

# Input: s = "banana"
# Output: "ana"
# Example 2:

# Input: s = "abcd"
# Output: ""
 

# Constraints:

# 2 <= s.length <= 3 * 104
# s consists of lowercase English letters.


# This solution works:


'''
If you familiar with Rabin-Karp algorighm, it will be not so difficult.
You can see it in full details on Wikipedia: https://en.wikipedia.org/wiki/Rabin–Karp_algorithm

Here I briefly explain the idea of it. Imagine, that we have string abcabcddcb, and we want to check if there are two substrings of size 3, which are equal. Idea is to hash this substrings, using rolling hash, where d is our base and q is used to avoid overflow.

for abc we evaluate [ord(a)*d^2 + ord(b)*d^1 + ord(c)*d^0] % q
for bca we evaluate [ord(b)*d^2 + ord(c)*d^1 + ord(a)*d^0] % q
Note, that we can evaluate rolling hash in O(1), for more details please see wikipedia.
...
However, it can happen that we have collisions, we can falsely get two substrings with the same hash, which are not equal. So, we need to check our candidates.

Binary search for help
Note, that we are asked for the longest duplicate substring. If we found duplicate substring of length 10, it means that there are duplicate substrings of lenths 9,8, .... So, we can use binary search to find the longest one.

Complexity of algorighm is O(n log n) if we assume that probability of collision is low.

How to read the code
I have RabinKarp(text, M,q) function, where text is the string where we search patterns, M is the length we are looking for and q is prime modulo for Rabin-Karp algorighm.

First, we need to choose d, I chose d = 256, because it is more than ord(z).
Then we need to evaluate auxiliary value h, we need it for fast update of rolling hash.
Evalute hash for first window
Evaluate hashes for all other windows in O(n) (that is O(1) for each window), using evaluated h.
We keep all hashes in dictionary: for each hash we keep start indexes of windows.
Finally, we iterate over our dictionary and for each unique hash we check all possible combinations and compare not hashes, but original windows to make sure that it was not a collision.
Now, to the longestDupSubstring(S) function we run binary search, where we run our RabinKarp funcion at most log n times.
'''
class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h, t, d = (1<<(8*M-8))%q, 0, 256

        dic = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            for j in dic[t]:
                if text[i+1:i+M+1] == text[j:j+M]:
                    return (True, text[j:j+M])
            dic[t].append(i+1)
        return (False, "")

    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found

