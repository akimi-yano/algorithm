# 354. Russian Doll Envelopes
# Hard

# 3514

# 84

# Add to List

# Share
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
 

# Constraints:

# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105


# This solution works:


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        [[2,3],[5,4],[6,4],[6,7]]
        [2,3], [5,4], [6,7]
        
        [[2,100],[3,200],[4,300],[5,250],[5,400],[5,500],[6,360],[6,370],[7,380]]
        '''
        # after sorting by reverse order for x[1], we can just look at height
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        arr = []
        for width, height in envelopes:
            i = bisect_left(arr, height)
            if i < len(arr):
                arr[i] = height
            else:
                arr.append(height)
        return len(arr)