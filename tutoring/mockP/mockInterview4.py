ref = {
    "a":7,
    "b":2,
    "c":1
}
import random


# ["a", "a" ... "b" "b" , "c"] x

# -> a 70%  b 20%  c %10


# 12345678910
# rand = randint (1,10) -> 6


# lower - 
# 1 - 7 - a
# 8 - 9 - b
# 10 - c


# 1-10
# start <= x <= end


#   ref = {
#     "a":2000,
#     "b":1000,
#     "c":7000
#   }

#   start = 1
#   keys = ["a", "b", "c"]
                # M                              
#   arr = [["h", 10], ["z", 1000], ["a", 2000],["b", 3000],["c", 10000]]

def randomizer(ref):
    keys = []
    arr = []
    sum = 0
    for k,v in ref.items():
        keys.append(k)
        sum+=v
        arr.append(sum)
    start = 1
    target = random.randint(1, arr[-1])
    for i in range(len(arr)):
        end = arr[i]
        if start <= target <= end:
            return keys[i]
        start = arr[i]
print(randomizer(ref))
# [0][1][2]

#   do it with binary search

# space : better than quadratic
# time : nlogn or less (maybe linear or logn)

# --------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def inOrder(root):
    current = root  
    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif(stack): 
            current = stack.pop() 
            print(current.val)
            current = current.right  
        else: 
            break


def inOrderR(root):
    stack = []
    def helper(current):
        if current:
            stack.append(current)
            helper(current.left)
            stack.pop()
            print(current.val)
            helper(current.right)
    helper(root)
    
    
    # next week
    
    # 1. [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
    # [
    #     [7,4,1],
    #     [8,5,2],
    #     [9,6,3]
    # ]
    
    # 2. Anagrams "bat" "abt" "tab"
    #     10 * 10 * 10 * 10
    
    # 3. [1,2,3] L, R
    
    
    
    
    