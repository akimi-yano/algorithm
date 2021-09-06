# 899. Orderly Queue
# Hard

# 413

# 302

# Add to List

# Share
# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

# Example 1:

# Input: s = "cba", k = 1
# Output: "acb"
# Explanation: 
# In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
# In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
# Example 2:

# Input: s = "baaca", k = 3
# Output: "aaabc"
# Explanation: 
# In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
# In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

# Constraints:

# 1 <= k <= s.length <= 1000
# s consist of lowercase English letters.


# This solution works:


class Solution:
        '''
        If K > 1 than we can change any two adjacent elements: first we can rotate our string, such that we have abX, where X is some string. Then we can put b to the end and then a to the end, rotate again and we have baX. Now we can look at it as an bubble sort: doing these moves we can sort all string. If K = 1 we allowed only rotate string and goal is to choose smallest one among n options.

        Complexity
        Time complexity is O(n^2) for time and O(n) for space
        '''
        def orderlyQueue(self, S, K):
            if K > 1: return "".join(sorted(S))
            return min(S[i:]+S[:i] for i in range(len(S)))