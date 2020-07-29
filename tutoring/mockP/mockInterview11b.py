# 658. Find K Closest Elements

# Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.


# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# Absolute value of elements in the array and x will not exceed 104

# this donest work - see at the bottom

# from collections import deque
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         left = 0
#         right = len(arr)-1
#         start = None
#         if x <= arr[left]:
#             start = left
#         elif x >= arr[right]:
#             start = right
#         else:
#             while left < right:
#                 mid = (left+right)//2
#                 if arr[mid] == x:
#                     start = mid
#                     break
#                 elif arr[mid] < x:
#                     left=mid+1
#                 else:
#                     right=mid-1
#             if not start:
#                 start = left
#         l=start-1
#         r=start+1
#         if l >= 0:
#             if abs(arr[l] - x) <= abs(arr[start] - x):
#                 start = l
#         if r < len(arr):
#             if abs(arr[r] - x) < abs(arr[start] - x):
#                 start = r
#         l=start-1
#         r=start+1
#         ans = deque([arr[start]])
        
#         left_val = None
#         right_val = None
#         while len(ans)<k:
#             if l>=0: 
#                 left_val=abs(arr[l]-x)
#             else:
#                 left_val = None
#             if r<=len(arr)-1:
#                 right_val=abs(arr[r]-x)
#             else:
#                 right_val = None 
#             if left_val is not None and right_val is not None:
#                 if left_val<=right_val:
#                     ans.appendleft(arr[l]) 
#                     l-=1
#                 else:
#                     ans.append(arr[r])
#                     r+=1
#             elif left_val is not None:
#                 ans.appendleft(arr[l])
#                 l-=1
#             elif right_val is not None:
#                 ans.append(arr[r])
#                 r+=1
#         return ans 
          

      
      
      
      
# # [1,2,4,5] 3
# s = Solution()
# # [2,3,4]
# # prepend / insert
# s.findClosestElements([1,2,3,4,5], 4, 3)
# s.findClosestElements([1,2,3,4,5], 4, -1)


# # print("Hello Pete san --- ")

# # Given a sorted array arr, two integers k and x, 
# # find the k closest elements to x in the
# # array. The result should also be sorted in ascending order.
# # If there is a tie, the smaller elements are always preferred.

# # Example 1:

# # Input: arr = [1,2,3,4,5], k = 4, x = 3
# # Output: [1,2,3,4]
# # Example 2:

# # Input: arr = [1,2,3,4,5], k = 4, x = -1
# # Output: [1,2,3,4]

# # Constraints:

# # 1 <= k <= arr.length
# # 1 <= arr.length <= 10^4
# # Absolute value of elements in the array and x will not exceed 10^4

# '''
# 1 where is x in arr? - exist or not ? binary search O(logN) find start 
# 2 from the start keep appending - queue in while loop until len(ans)<k
# log(log+k)

# '''
# from collections import deque
# class Solution:
#     def findClosestElements(self, arr, k, x):
#       # binary search
#       left = 0
#       right = len(arr)-1
#       start = None
#       # check left and right
#       if x <= arr[left]:
#         start = left
#       elif x >= arr[right]:
#         start = right
#       else:
#         while left < right:
#           mid = (left+right)//2
#           if arr[mid] == x:
#             start = mid
#             break
#           elif arr[mid] < x:
#             left=mid+1
#           else:
#             right=mid-1
#         if not start:
#           start = left
      
#       ans = deque([arr[start]])
#       l=start-1
#       r=start+1
#       left_val = None
#       right_val = None
#       while len(ans)<k:
#         # compare abs distance from x on left and right
#         #   gives us which candidate
#         #     which pointer to move
#         if l>=0: 
#           left_val=abs(arr[l]-x)
#         else:
#           left_val = None
#         if r<=len(arr)-1:
#           right_val=abs(arr[r]-x)
#         else:
#           right_val = None 
          
#           if left_val and right_val:
#             if left_val<right_val:
#               ans.appendleft(arr[l]) 
#               l-=1
#             else:
#               ans.append(arr[r])
#               r+=1
#           elif left_val:
#             ans.appendleft(arr[l])
#             l-=1
#           else:
#             ans.append(arr[r])
#             r+=1
        
#       return ans 
            
            # -----------------------
            
            
            
# this works

from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr[0] >= x:
            return arr[:min(k, len(arr))]
        elif arr[-1] <= x:
            return arr[-min(k, len(arr)):]
        elif len(arr) < 2:
            return arr
        
        left = 0
        right = len(arr)-1
        while left + 1 < right:
            mid = (left+right) // 2
            if arr[mid] > x:
                right = mid
            else:
                left = mid

        ans = deque([])

        while len(ans) < k and left >= 0 and right < len(arr):
            if x-arr[left] <= arr[right] - x:
                ans.appendleft(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1

        while len(ans) < k and left >= 0:
            ans.appendleft(arr[left])
            left -= 1
        while len(ans) < k and right < len(arr):
            ans.append(arr[right])
            right += 1

        return list(ans)
      
# [1,2,4,5] 3
s = Solution()
# [2,3,4]
# prepend / insert
s.findClosestElements([1,2,3,4,5], 4, 3)
s.findClosestElements([1,2,3,4,5], 4, -1)
