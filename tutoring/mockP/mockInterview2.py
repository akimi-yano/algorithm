
    
"""
n = 5

*****
*   *
*   *
*   *
*****

"""

def abc(n) -> None:
    for i in range(n):
        if i == 0 or i == n-1:
            print("*"*n)
        else:
            print("*"+(" "*(n-2))+"*")

"""

input : int n
output : print 

- * surrounding empty inside 
col = row = n

 for loop - row
 for loop - col 
 
 row 1 all col
 row 2- 4 just start and end  - rest is space
 row 5 (last) all col 

"!" * 5 -> "!!!!!"

"""

# Kadane's Algorithm
# Greedy approach for array and finding max contiguous subarray
"""
[1, 2, 3, 2, 4, 5]
-> [2,2,1,3,4,5]

[1, 2, 3, 2, 4, 4, 4, 5]


-> [1,3,5,2,2,4,4,4]
n * n log n
sorted(array, key=lambda x: x) -> sorts elements by value
sorted(array, key=lambda x: len(x)) -> ''' ( ͡° ͜ʖ ͡°)
"""

def bcd(array):
    memo = {}
    ans = []
    #  頑張ってください ( •̀ᴗ•́ )و ̑̑ (๑￫ܫ￩)
    for num in array:
        if num not in memo:
            memo[num] = 1 
        else:
            memo[num] += 1

    i = 1
    # how to know? ʕ·ᴥ·　ʔ
    # elements = 0
    elements = max(memo.values())
    # for k, v in memo.items():
    #     if v > elements:
    #         elements = v
    # elements is now max count
    for i in range(elements):
        ans.append([])
    a = set(array)
    a = list(a)
    a = sorted(a, key=lambda x:x)
    # [1,2,3,4,5,7,8]
    # print(a)
    for i in a:
        value = memo[i]
        for j in range(value):
            ans[value-1].append(i)
    # for k,v in memo.items():
        # for i in range(v):
            # ans[v-1].append(int(k))
    
    # for i in range(len(ans)):
        # ans[i] = sorted(ans[i], key=lambda x:x)
    # you can just reverse the array
    result = []
    ans.reverse()
    for i in ans:
        if len(i) > 0:
            for j in i:
                result.append(j)
    # print(result)
    # while i < len(array):
    #     temp = []
    #     for k, v in memo.items():
    #         if v == i: #  υ(´• ﻌ •`)υ
    #             temp.append(k)
    #     temp = sorted(temp)
    #     ans.extend(temp)
    #     i+=1
    return result
# [[],[],[],[],[],[]] ?
# [[1,3,5],[2,2],[4,4,4],[7,7,7,7],[],[8,8,8,8,8,8]]

print(bcd([3,2,1,2,4,4,4,5,7, 7, 7, 7,8,8,8,8,8,8]))
"""
loop the array count and save the count in the dictionary

memo = {4:3, 2:2, 1:1, 3:1, 5:1}
min_freq = 1
3 - 4 - append

1 - 1,3,5 
2 - 2 

"""

# array.sort((a, b) => a-b)
# array = sorted(array, key=lambda x: x["temp"], reversed=True)










