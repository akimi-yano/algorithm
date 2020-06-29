# check-if-array-pairs-are-divisible-by-k	
# [Check If Array Pairs Are Divisible by k https://leetcode.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/]
# mod k の値のみに注目し、基本的には i と k-i の個数が等しいかを check。i = 0のときと、k が偶数のときは i = k/2 のときは別に処理しないといけない。


# this doesnt work - look below solution that works !
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         # choose 2 numbers out of the set
#         # add them and check if it is divisible by k
#         # delete them from the arr/set

#         from collections import deque
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:

#         queue = deque([])
#         arr.sort()
#         left = 0
#         right = len(arr)-1
#         count = 0
#         while count<len(arr)//2:
#             print(arr)
#             if (arr[left]+arr[right])%k == 0:
#                 queue.popleft()
#                 queue.pop()
#             count+=1
#         if len(arr)==0:
#             return True
#         else:
#             return False


# this works
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # mod k の値のみに注目し、基本的には i と k-i の個数が等しいかを check。
        # i = 0のときと、k が偶数のときは i = k/2 のときは別に処理しないといけない
        
        memo = {}
        for num in arr:
            val = num % k
            if val not in memo:
                memo[val] = 1
            else:
                memo[val] +=1
        
        for key,value in memo.items():
            if key == 0:
                if value%2!=0:
                    return False
            elif (k-key) not in memo:
                return False
            else:
                if key == (k-key):
                    if memo[key]%2!=0:
                        return False
                if memo[key]!=memo[(k-key)]:
                    return False
        return True








