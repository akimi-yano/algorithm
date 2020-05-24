class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def helper(n1, n2):
            
            # cant do dot product if one of the arr is empty so return 0
            if len(n1) < 1 or len(n2) < 1:
                return 0
            
            # define the first element of each array
            num1 = n1[0]
            num2 = n2[0]
            
            # we put the length of each array to keep track of the best dot products of the given arrays
            if (len(n1), len(n2)) in memo:
                return memo[(len(n1), len(n2))]
            
            best = 0
            # its better off to get dot droduct if both numbers are positive or both are nevative
            if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0):
                # the case where we move forward both of them
                best = num1 * num2 + helper(n1[1:], n2[1:])
            # the case where we move forward just n2 array
            best = max(best, helper(n1, n2[1:]))
            # the case where we move forward just n1 array
            best = max(best, helper(n1[1:], n2))
            
            # put the best dot product value as value and the key based on the length of the arrays
            memo[(len(n1), len(n2))] = best
            return best

        # this is not in the recursion part
        # edge case 1: everything in nums1 is less than 0, and everything in nums2 is greater than zero
        a = reduce(lambda x, y: x and y, [n < 0 for n in nums1])
        b = reduce(lambda x, y: x and y, [n > 0 for n in nums2])
        if a and b:
            # get max for negative list and get min for positive list
            return max(nums1) * min(nums2)
        # edge case 2: everything in nums1 is greater than 0, and everything in nums2 is less than zero
        c = reduce(lambda x, y: x and y, [n > 0 for n in nums1])
        d = reduce(lambda x, y: x and y, [n < 0 for n in nums2])
        if c and d:
            # get min for positive list and get max for negative list
            return min(nums1) * max(nums2)
        
        # else: do recursion to find the best dot product
        return helper(nums1, nums2)
        