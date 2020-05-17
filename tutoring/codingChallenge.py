# [Completed]
# 1 given an unsorted array of integers, each integer is repeated twice except for one of them. 
# find and return the integer that is not duplicated
# try without constraints
# try with memory constraint -> dont use additional structures (look up bitwise)

def findUnique(arr):
    result = arr[0]
    # print(bin(result))
    for i in range(1,len(arr)):
        result^=arr[i]
        # print(bin(result))
    return result
# print(findUnique([1,0,0,2,1]))
# print(findUnique([1,0,6,0,5,1,6]))
# print(findUnique([1,2,2,1,3,4,4,3,5,6,6,7,7]))
# a=1
# b=2
# a^=b
# print("a ^ b =",a )
# 1 = 0001
# 2 = 0010
# 0011 = 3

#2 you are provided with a number N, find the pattern given these examples:
# if n == 0: return 0 - 
# if n == 1: return 1 -
# if n == 9: return 9 - 

# (in the actual interview, these will be the only example given!)
# if n == 10: return 19 - 
# if n == 19: return 199 - 
# return the correct result given the number N

def findPattern(n):
    ans = "" + str(n%9) + str("9"*(n//9))
    return int(ans)
# print(findPattern(10))
# print(findPattern(19))
# print(findPattern(1))
# print(findPattern(9))
for num in range(22):
    print(findPattern(num))



# solutions:
    
# basically it's counting by 9
# starts at 0
# and once 9 fills up
# instead of going to 10
# it stops there and carries over to the next
# so 10 -> 19
# ur just adding a 1
# to the front
# so 11 -> 29
# and 12 -> 39
# which means now there is a few ways to handle this
# but u can divide the number against 9
# to get the number of 9's in the back side
# and whatever remainder of 9 is on the front
# so there are two 9's
# 18 / 9 == 2
# two nines
# 18 % 9 == 0
# there's a zero in the front of that number
# in python u can use multiplication on a string to repeat it
# "" + (str(n % 9)) + ( "9" * (n // 9))
# and then use int() to convert it to a number
# can also do iterations to calculate the pattern as well


#3 you are provided with a string of undetermined length. 
# it has only uppercase letters (no numbers, no special characters). 
# figure out how many times the word "BALLOON" can be extracted from the string. return the count.
def countBaloon(str):
    memo = {'B':0, 'A':0, 'L':0,'O':0,'N':0}
    for i in range(len(str)):
        if str[i] not in memo: 
            memo[str[i]]=1
        else:
            memo[str[i]]+=1
    memo['L']=memo['L']//2
    memo['O']=memo['O']//2
    return min(memo.values())
#     for key,value in memo.items():
#         print(key, value) 
# print(countBaloon('BALLOONBALLOONBALLOONBALLON'))

        

