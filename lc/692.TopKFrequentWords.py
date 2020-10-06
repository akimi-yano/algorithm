# 692. Top K Frequent Words
# Medium

# 2252

# 159

# Add to List

# Share
# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


# This solution works : 
# Time: O(NlogN)
# Space: O(N)

# from collections import Counter
class Solution1:
    def topKFrequent1(self, words, k):
        counts = Counter(words)
        temp = []
        for key, val in counts.items():
            temp.append((val, key))
        temp.sort(key = lambda elem: (-elem[0], elem[1]))
        return [elem[1] for elem in temp[:k]]


# This solution works : 



class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return (self.freq  <  other.freq) # self.freq < other.freq
        else:
            # opposite sort
            return (other.word  <  self.word) # other.word < self.word
        
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        words_with_count = Counter(words)
            
        min_heap = []
        for word, count in words_with_count.items():
            heapq.heappush(min_heap, FreqWord(count, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [heapq.heappop(min_heap).word for _ in range(k)][::-1]   
    
s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)) # ["i", "love"]
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)) # ["the", "is", "sunny", "day"]