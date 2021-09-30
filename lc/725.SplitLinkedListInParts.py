# 725. Split Linked List in Parts
# Medium

# 1384

# 169

# Add to List

# Share
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

 

# Example 1:


# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:


# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

# Constraints:

# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50


# This solution works:


'''
Just do what is asked carefully: first, find number of nodes N in our list and evaluate d and r: how many times nodes there should be in the first part minus one. Then we can evaluate number of nodes in every part, using formula d + (i < r) - 1, where i goes from 0 to k-1. In each part, we do d (or d-1 steps), so now we are in the end of this part. If we are not at the None node (so, if part has at least one element), then we cut connection between current node and next one and go to the next node.

Complexity
Time complexity is O(n + k), because it can happen that k is much bigger than n. Space complexity is O(k) to write answer.

'''
class Solution:
    def splitListToParts(self, root, k):
        cur = root
        N = 0
        while cur:
            cur = cur.next
            N += 1
        d, r = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(d + (i < r) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
