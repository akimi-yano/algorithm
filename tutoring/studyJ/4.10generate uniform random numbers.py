# 4.10 generate uniform random numbers

# this does not work

# import random
# def rand_generator(upper,lower):
#     binary = random.randint(0,1)
#     res = 0
#     b_digit = len(bin(upper))-2
#     while b_digit>0:
#         res<<=1
#         res+=res^binary
#         b_digit-=1
#     # print(res)
#     if lower<=res<=upper:
#         return res
#     return 
# print(rand_generator(0,5))

import random

def uniform_random(lower_bound,upper_bound):
    def zero_one_random():
        return random.randint(0,1)
    
    number_of_outcomes = upper_bound - lower_bound +1
    while True:
        result, i = 0, 0
        while (1 << i) <number_of_outcomes:
            #zero_one_random() is the provided random number generator
            result = (result<<1) | zero_one_random()
            i+=1
        if result<number_of_outcomes:
            break
    return result + lower_bound

print(uniform_random(0,6))