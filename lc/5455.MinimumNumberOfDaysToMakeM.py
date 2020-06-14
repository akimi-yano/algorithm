# 5455. Minimum Number of Days to Make m Bouquets
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         if m*k > len(bloomDay):
        #     return -1
        # temp = []
        # for i in range(len(bloomDay)):
        #     temp.append((bloomDay[i],i))
        # temp.sort(key = lambda x: (-x[0],-x[1]))
        # # print(temp)
      
        # idx = len(temp)-1
        # while idx>-1 and m>0:
        #     t = k 
        #     while t>0:
        #         day = temp[idx][0]
        #         temp.pop()
        #         t-=1
        #         m-=1
        #     idx-=1        
        # if m>0:
        #     return -1
        # return day
        
# O(NlogR)
def minDays(bloomDay, m, k):
    head = 0
    tail = 10**9 +5
    # O(N)
    def  good(x):
        count =0
        run =0
        for day in bloomDay:
            if x >=day:
                run+=1
            else:
                run =0
            if run>=k:
                count+=1
                run = 0
        return count >= m
    # O(logR) - binary search
    while head < tail:
        mid = (head+tail)//2
        if good(mid):
            tail = mid
        else:
            head = mid+1
    if head > max(bloomDay):
        return -1
    return head 
print(minDays([7,7,7,7,12,7,7],2,3))