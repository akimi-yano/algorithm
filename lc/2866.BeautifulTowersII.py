'''
2866. Beautiful Towers II
Medium
180
11
Companies
You are given a 0-indexed array maxHeights of n integers.

You are tasked with building n towers in the coordinate line. The ith tower is built at coordinate i and has a height of heights[i].

A configuration of towers is beautiful if the following conditions hold:

1 <= heights[i] <= maxHeights[i]
heights is a mountain array.
Array heights is a mountain if there exists an index i such that:

For all 0 < j <= i, heights[j - 1] <= heights[j]
For all i <= k < n - 1, heights[k + 1] <= heights[k]
Return the maximum possible sum of heights of a beautiful configuration of towers.

 

Example 1:

Input: maxHeights = [5,3,4,1,1]
Output: 13
Explanation: One beautiful configuration with a maximum sum is heights = [5,3,3,1,1]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i]  
- heights is a mountain of peak i = 0.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 13.
Example 2:

Input: maxHeights = [6,5,3,9,2,7]
Output: 22
Explanation: One beautiful configuration with a maximum sum is heights = [3,3,3,9,2,2]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i]
- heights is a mountain of peak i = 3.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 22.
Example 3:

Input: maxHeights = [3,2,5,5,2,3]
Output: 18
Explanation: One beautiful configuration with a maximum sum is heights = [2,2,5,5,2,2]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i]
- heights is a mountain of peak i = 2. 
Note that, for this configuration, i = 3 can also be considered a peak.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 18.
 

Constraints:

1 <= n == maxHeights <= 105
1 <= maxHeights[i] <= 109
'''

class Solution:
    def maximumSumOfHeights(self, maxHeights):
        n = len(maxHeights)
        
        def make(maxHeights):
            ans = [0]
            stack = []
            total = 0
            for i in range(n):
                width = 1
                while stack and maxHeights[i] <= maxHeights[stack[-1][0]]:
                    i0, w0 = stack.pop()
                    total -= maxHeights[i0] * w0
                    width += w0
                
                stack.append([i, width])
                total += maxHeights[i] * width
                ans.append(total)

            return ans
        
        left = make(maxHeights)
        right = make(maxHeights[::-1])[::-1]
        return max(left[i] + right[i] for i in range(n + 1))

'''
Let's try to compute left[i] as the largest sum of heights for a tower that has peak at i and only goes left.

This tower is composed of sections, each section has height maxHeights[i] and width w, and we can store these sections (with necessarily increasing height) in stack and maintain them as we increase i.

In particular, we destroy any section that is higher than maxHeights[i] by popping from the stack, then we construct a new section with width. total keeps track of the total area of the tower.
'''


class Solution:
    def maximumSumOfHeights(self, maxHeights):
        '''
        [5,3,4,1,1]
         0 1 2 3 4

         if 2 is the peak:
             itsLeftIfiIsPeak : [3 3 4 <- strictly increasing
             itsReftIfiIsPeak : 4 1 1] <- strictly decreasing (can reverse)
            3+3+4+1+1 (+4-4 as we added the peak twice) 
        '''
        N = len(maxHeights)

        # LEFT SIDE:
        itsLeftAndSelfIfiIsPeak = [] # save the total of left side if the peak is at i :[] -> [5] -> [5, 6] -> [5, 6, 10]
        monostack = [] # strickly increasing value's i and width :[] -> [0] -> [1] -> [1,2] -> [0,1] -> [0] * width is ommited here in this comment
        leftTotalIfiIsPeak = 0 
        for i in range(N): # : 0
            width = 1
            while monostack and maxHeights[i] < maxHeights[monostack[-1][0]]:
                # : monostack is empty
                j, w = monostack.pop()
                leftTotalIfiIsPeak -= maxHeights[j] * w
                width += w
                
            leftTotalIfiIsPeak += maxHeights[i] * width
            itsLeftAndSelfIfiIsPeak.append(leftTotalIfiIsPeak)
            monostack.append([i, width])
        print(itsLeftAndSelfIfiIsPeak)

        # RIGHT SIDE:
        itsRightAndSelfIfiIsPeak = [] 
        monostack = [] # strickly increasing value's i and width
        rightTotalIfiIsPeak = 0 
        maxHeights = maxHeights[::-1]
        for i in range(N): 
            width = 1
            while monostack and maxHeights[i] < maxHeights[monostack[-1][0]]:
                # : monostack is empty
                j, w = monostack.pop()
                rightTotalIfiIsPeak -= maxHeights[j] * w
                width += w
                
            rightTotalIfiIsPeak += maxHeights[i] * width
            itsRightAndSelfIfiIsPeak.append(rightTotalIfiIsPeak)
            monostack.append([i, width])
        itsRightAndSelfIfiIsPeak = itsRightAndSelfIfiIsPeak[::-1]
        
        # CALCULATE THE TOTAL:
        maxHeights = maxHeights[::-1]
        best = 0
        for k in range(N):
            total = itsLeftAndSelfIfiIsPeak[k]+itsRightAndSelfIfiIsPeak[k]-maxHeights[k]
            best = max(best, total)
        return best