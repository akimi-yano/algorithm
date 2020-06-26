# 287 Find the Duplicate Number  

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
# # In this problem, nums[a] = b can be seen as a.next = b, the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.
#         slow = fast = finder = 0
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 while finder != slow:
#                     finder = nums[finder]
#                     slow = nums[slow]
#                 return finder

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # print('...')
        N = len(nums) - 1
        left = 1
        right = N
        while left < right:
            mid = (left + right) // 2
            # print('Searching (left={}-{}, right={}-{})'.format(left, mid, mid+1, right))
            left_counter = 0
            right_counter = 0
            for num in nums:
                if left <= num <= mid:
                    left_counter += 1
                elif mid < num <= right:
                    right_counter += 1

            # if there are more numbers than there should be on the left side, the duplicate must be
            # on the left side
            if left_counter > (mid-left+1):
                # print('found {} numbers on left side({}-{})'.format(left_counter, left,mid))
                # 
                right = mid
            # otherwise, it must be on the right side
            else:
                # print('found {} numbers on right side({}-{})'.format(right_counter, mid+1,right))
                left = mid + 1
        return left