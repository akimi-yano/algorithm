import sys

# This solution works:
# from functools import lru_cache
al_i = {}
i_al = {}
for i in range(26):
    al_i[chr(ord('A')+i)] = i
    i_al[i] = chr(ord('A')+i)

def helper(arr):
    # @lru_cache(None)
    def helper2(i, prev):
        if not 0 <= prev < 26:
            return None
        if i > len(nums)-1:
            return []

        ans = []
        # increasing
        if nums[i]:
            for cur in range(prev+1, 26):
                maybe = helper2(i+1, cur)
                if maybe is not None:
                    maybe.append(cur)
                    return maybe
            return None
        # decreasing
        else:
            for cur in range(0, prev):
                maybe = helper2(i+1, cur)
                if maybe is not None:
                    maybe.append(cur)
                    return maybe
            return None

    nums = []
    for j in range(len(arr)):
        for _ in range(arr[j]):
            nums.append(0) if j%2 else nums.append(1)

    res = ['A'] + [i_al[n] for n in reversed(helper2(0, 0))]
    # helper2.cache_clear()
    return "".join(res)
        
    
num_tests = int(next(sys.stdin))
for i in range(num_tests):
    next(sys.stdin)
    arr = [int(elem) for elem in next(sys.stdin).strip().split()]
    print(f'Case #{i+1}: {helper(arr)}')




# This approach does not work:

# import sys
# from functools import lru_cache
# al_i = {}
# i_al = {}
# for i in range(26):
#     al_i[chr(ord('A')+i)] = i
#     i_al[i] = chr(ord('A')+i)

# def helper(arr):
#     @lru_cache(None)
#     def helper2(i, prev):
#         if i > len(nums)-1:
#             return [[]]

#         ans = []
#         # increasing
#         if nums[i]:
#             for c in range(al_i[prev]+1, 26):
#                 ans.extend( [i_al[c]] + temp for temp in helper2(i+1, i_al[c]))
        
#         # decreasing
#         else:
#             for c in range(0, 26):
#                 if al_i[prev] > c:
#                     ans.extend( [i_al[c]] + temp for temp in helper2(i+1, i_al[c]))
#         return ans

#     nums = []
#     for j in range(len(arr)):
#         for _ in range(arr[j]):
#             nums.append(0) if j%2 else nums.append(1)

#     res = ['A'] + helper2(0, 'A')[0]
#     return "".join(res)
        
    
# num_tests = int(next(sys.stdin))
# for i in range(num_tests):
#     next(sys.stdin)
#     arr = [int(elem) for elem in next(sys.stdin).strip().split()]
#     print(f'Case #{i+1}: {helper(arr)}')

