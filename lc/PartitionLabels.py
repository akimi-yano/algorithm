# Partition Labels

# Solution
# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


# Note:

# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.



# This solution works !


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        for s in S:
            if s not in count:
                count[s] = 1
            else:
                count[s] += 1

        d = {}
        ans = []
        start = 0
        for i, s in enumerate(S):
            if s not in d:
                d[s] = 0
            d[s]+=1
            if d[s] == count[s]:
                del d[s]
            if len(d) == 0:
                ans.append(i-start+1)
                start = i+1
        return ans 
    
    
# This is closer to my original solution:

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, c in enumerate(S):
            last[c] = i
        # print("Last indexes: {}".format(last))
        
        current_group = set([])
        
        last_group_end = -1
        ans = []
        
        for i, c in enumerate(S):
            current_group.add(c)
            # print("[{}]Group so far: {}".format(i, current_group))
            if i == last[c]:
                # print("  removing {}".format(c))
                current_group.remove(c)
            if len(current_group) < 1:
                # print("Group found! Starting new group...")
                ans.append(i-last_group_end)
                last_group_end = i
        return ans