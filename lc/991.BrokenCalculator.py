# 991. Broken Calculator
# Medium

# 745

# 118

# Add to List

# Share
# On a broken calculator that has a number showing on its display, we can perform two operations:

# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.

# Return the minimum number of operations needed to display the number Y.

 

# Example 1:

# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# Example 2:

# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# Example 3:

# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
# Example 4:

# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
 

# Note:

# 1 <= X <= 10^9
# 1 <= Y <= 10^9


# This approach does not work:
# import heapq
# class Solution:
#     def brokenCalc(self, X: int, Y: int) -> int:
#         minheap = []
#         heapq.heappush(minheap,(0, X))
#         seen = set([])
#         while minheap:
#             step, val = heapq.heappop(minheap)
#             if val == Y:
#                 return step
#             if val in seen:
#                 continue
#             seen.add(val)
#             if val < Y:
#                 heapq.heappush(minheap,(step+1, val*2))
#             heapq.heappush(minheap,(step+abs(Y-val), Y))
                


# This solution works:

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        max_multiplier = 1
        
        ops = 0
        X_mult2 = X
        while X_mult2 < Y:
            max_multiplier *= 2
            X_mult2 *= 2
            ops += 1
        
        difference = X_mult2 - Y
        while difference > 0:
            num_used, difference = divmod(difference, max_multiplier)
            ops += num_used
            max_multiplier //= 2
        return ops