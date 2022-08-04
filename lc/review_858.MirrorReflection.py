# 858. Mirror Reflection
# Medium

# 575

# 1268

# Add to List

# Share
# There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

# The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

# Given the two integers p and q, return the number of the receptor that the ray meets first.

# The test cases are guaranteed so that the ray will meet a receptor eventually.

 

# Example 1:


# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
# Example 2:

# Input: p = 3, q = 1
# Output: 1
 

# Constraints:

# 1 <= q <= p <= 1000


# This solution works:


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        right = False
        y = 0
        delta = q
        while True:
            y += delta
            right ^= True
            if y > p:
                y -= (y-p) * 2
                delta *= -1
            elif y < 0:
                y += (-y) * 2
                delta *= -1
            
            if y == p:
                if right:
                    return 1
                else:
                    return 2
            if y == 0:
                if right:
                    return 0
                # delta *= -1