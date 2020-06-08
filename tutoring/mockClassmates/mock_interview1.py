# turn input int into string type
# make a dictionary 
# ans set 
# recursion solution - initialize with helper([],0)
# base case - checked all the numbers
# is in in doctionary ? check all
# recursive - helper(arr+nums[i],i+1) 65489168546 


def letterCombinations(nums):
    nums = str(nums)
    if len(nums)==0:
        return []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    dict = {} #key - number - value - alpha letters
    k=0
    for i in range(2,10):
        if i ==7 or i==9:
            dict[str(i)]=[alpha[k],alpha[k+1],alpha[k+2],alpha[k+3]]
            k+=4
        else:
            dict[str(i)]=[alpha[k],alpha[k+1],alpha[k+2]]
            k+=3
        # print(dict)
    ans  = set([])

    def helper(word, i):
        if i >len(nums)-1:
            ans.add(word)
            return 

            # print(nums[i])
        if nums[i] in dict:
            for letter in dict[nums[i]]:
                helper(word+letter,i+1)
        else:
            helper(word,i+1)
    helper("",0)

    ans = list(ans)
    return ans

print(len(letterCombinations(2217)))
print(letterCombinations(2217))

  # input - 227
  
  # arr [aap]
  # ans = ['aap']
  
  
  
