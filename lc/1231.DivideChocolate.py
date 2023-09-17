'''
1231. Divide Chocolate
Hard
930
53
company
Google
company
Amazon
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

Constraints:

0 <= k < sweetness.length <= 104
1 <= sweetness[i] <= 105
'''


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        def isValid(myChoco):
            cuts = 0
            chunk_sweetness = 0
            for piece in sweetness:
                chunk_sweetness += piece
                # what if there is another chunk_sweetness == mid beside my own? -> It is ok as long as mine is minimum (there can be multiple chunks of minimum like in the Example 3)
                if chunk_sweetness >= mid:
                    cuts += 1
                    chunk_sweetness = 0
            return cuts >= k+1

        left = min(sweetness)
        # Realise that each chunk can have at least 1 sweetness (mentioned in the constraint) and at most high = total sweetness / chunks needed which is sum(sweetness) / (K + 1). K friends + yourself -> K+1 chunks.
        right = sum(sweetness) // (k+1)
        
        while left < right:
            # make sure to not infinite loop as I am not infinite loop 
            # ex) if left == 0 and right == 1 => mid = 0 and left is 0 again
            # so add + 1 as (left is not moving)
            mid = (left + right + 1) // 2
            if isValid(mid):
                left = mid
            else:
                right = mid - 1
        return left
        


'''
Approach Note:

- Realise that each chunk can have at least 1 sweetness (mentioned in the constraint) and at most high = total sweetness / chunks needed which is sum(sweetness) / (K + 1). 
K friends + yourself -> K+1 chunks.

- Use binary search to quickly find the target sweetness which is the maximum sweetness possible when we make K cuts ("cutting the chocolate bar optimally"). 
Then find the minimum sweetness out of the chunks we have.

- As long as low < high: we check the mid level of sweetness: mid = floor((low + high + 1) / 2). Here +1 because we have to include mid level if it is the target sweetness. 
If we don't include +1, we'll be stuck in an infinite loop because we'll always pick the same mid point which is the low.

- Once we pick the target (mid level of sweetness), we iterate through the sweetness array and calculate each chunk's sweetness. 
Once we reach or go over the target sweetness (mid), we increment the number of cuts and reset the chunk sweetness to 0 to start calculating the next chunk's sweetness.

- If with the current target, we end up having more cuts than needed, then we know we need to increase the level of sweetness, we look at the right half of the possible levels of sweetness for each chunk. 
Note, here we move low to mid because we need to include mid as a possible answer and eventually we return low. 
Otherwise, we need to decrease the level of sweetness, we move high to mid - 1 to look at the left half of the levels of sweetness for each chunk.

Time: O(nlog(10^9)) or O(nlog(m)) where n = len(sweetness) and m = range from 1 to high range (inclusive) because:

Binary search against the range low high levels of sweetness of each chunk: O(log(m)). 
Each time we pick a target sweetness, we iterate through input array: O(n) -> Total: O(nlog(m))
Space: O(1) because we don't use auxiliary space.
'''