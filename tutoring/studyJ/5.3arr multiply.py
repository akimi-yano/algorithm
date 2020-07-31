# 5.3 arr multiply 

# this does not work

# def multiply_num(arr1,arr2):
#     ans=[]
#     carry=0
#     for i in range(len(arr2)-1,-1,-1):
#         for j in range(len(arr1)-1,-1,-1):
#             print(arr1[i],arr2[j])
#             if len(ans)<i+1:
#                 ans.append(0)
#             temp =arr1[j]*arr2[i] + carry
#             print(ans)
#             ans[i+len(arr2)]+=temp%10
#             carry=temp//10
            
#     return ans
        
# # print(multiply_num([1,2,3],[4,1,6]))


# this works except for negative numbers

def multiply(arr1,arr2):
    def add_to_ans(ans, digit, loc):
        if loc >= len(ans):
            ans.append(digit)
            return
        carry, ans[loc] = divmod(ans[loc]+digit, 10)
        if carry > 0:
            add_to_ans(ans, carry, loc+1)

    ans = []
    for i, n1 in enumerate(reversed(arr1)):
        carry = 0
        for j, n2 in enumerate(reversed(arr2)):
            value = n1 * n2 + carry
            carry, digit = divmod(value, 10)
            add_to_ans(ans, digit, i+j)
        if carry > 0:
            add_to_ans(ans, carry, i+len(arr2))
    ans.reverse()
    return ans
    
# print(multiply([1,2,3],[4,1,6]))
# print(multiply([-1,2,3],[4,1,6])) it doesnt not work for negatives -----


# official answer

def multiply_official(num1,num2):
    sign = -1 if (num1[0]<0) ^ (num2[0]<0) else 1
    num1[0],num2[0]=abs(num1[0]),abs(num2[0])
    
    result=[0]*(len(num1)+len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1]+=num1[i]*num2[j]
            result[i+j]+=result[i+j+1]//10
            result[i+j+1]%=10
            
    # remove the leading zeroes
    result = result[next((i for i,x in enumerate(result)
                            if x!=0),len(result)):] or [0]
    
    return [sign*result[0]]+result[1:]

print(multiply_official([1,2,3],[4,1,6]))
print(multiply_official([-1,2,3],[4,1,6]))
print(multiply_official([1,2,3],[-4,1,6]))
print(multiply_official([-1,2,3],[-4,1,6]))











