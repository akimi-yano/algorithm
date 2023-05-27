'''
88. Merge Sorted Array
Easy
10.5K
1K
Companies
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = j = 0
        
        while m and n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                m -= 1
                i += 1
            else:
                temp.append(nums2[j])
                n -= 1
                j += 1
                
        while m:
            temp.append(nums1[i])
            m -= 1
            i += 1
            
        while n:
            temp.append(nums2[j])
            n -= 1
            j += 1
            
        for k in range(len(temp)):
            nums1[k] = temp[k]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        start making the sorted arr from the back of the arr nums1
        by comparing the larget of each arr
        
        case1:
        nums1[1,2,0,0] num2[1,2]
        m = 2 n = 2
        
        case2:
        nums1[0,0] num2[1,2]
        m = 0 n = 2
        
        case3:
        nums[1] nums2[0]
        m = 1 n = 0
        -> dont need to do anything
        '''
        insert_idx = m+n-1
        while m > 0 and n > -0:
            if nums1[m-1] > nums2[n-1]:
                nums1[insert_idx] = nums1[m-1]
                m -= 1
            else:
                nums1[insert_idx] = nums2[n-1]
                n -= 1
            insert_idx -= 1
          
        while n > 0:
            nums1[insert_idx] = nums2[n-1]
            n -= 1
            insert_idx -= 1