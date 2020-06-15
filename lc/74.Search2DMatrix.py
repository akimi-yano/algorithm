# 74. Search a 2D Matrix
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     if len(matrix)==0 or len(matrix[0])==0:
    #         return False
    #     # print(len(matrix[0]))
    #     low = 0
    #     high = len(matrix)-1
    #     mid = (low+high)//2
    #     while low<high:
    #         mid = (low+high)//2
    #         if matrix[mid][len(matrix[0])-1]==target:
    #             return True
    #         elif matrix[mid][len(matrix[0])-1]<target:
    #             low=mid+1
    #         else:
    #             high=mid
    #     # print(low)
    #     lo = 0
    #     hi = len(matrix[low])-1
    #     mi = (lo+hi)//2
    #     while lo<hi:
    #         mi = (lo+hi)//2
    #         if matrix[low][mi] == target:
    #             return True
    #         elif matrix[low][mi]<target:
    #             lo=mi+1
    #         else:
    #             hi=mi
    #     if matrix[low][lo] == target:
    #         return True 
    #     return False
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
                return False

        l = 0
        r = len(matrix)*len(matrix[0])

        while l<r:
            mid = (l+r)//2
            i = mid//len(matrix[0]) 
            j = mid%len(matrix[0])
            
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r = mid
            else:
                l = mid + 1

        return False
    
# learnings:
# (1) why not len(grid[0])-1?
# %4 -> the answer is 0-3
# //4 -> the answer is : 0-3 = 0
#                        4-7 = 1
# so dont do len(grid[0])-1 but fo len(grid[0])
# use column number for row and col

# (2) why not % for the row?
# since we are doing binary search, you dont wanna go back to beginning when you hit the end

# (3) why not high = len(grid)*len(grid[0]) -1 but  high = len(grid)*len(grid[0]) ?
# since they are just deciding the range and mid point for the further caluration with ?? and %,
# never go out of matrix bound so its ok