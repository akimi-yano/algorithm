# A. XORinacci
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Cengiz recently learned Fibonacci numbers and now he is studying different algorithms to find them. After getting bored of reading them, he came with his own new type of numbers that he named XORinacci numbers. He defined them as follows:

# 𝑓(0)=𝑎;
# 𝑓(1)=𝑏;
# 𝑓(𝑛)=𝑓(𝑛−1)⊕𝑓(𝑛−2) when 𝑛>1, where ⊕ denotes the bitwise XOR operation.
# You are given three integers 𝑎, 𝑏, and 𝑛, calculate 𝑓(𝑛).

# You have to answer for 𝑇 independent test cases.

# Input
# The input contains one or more independent test cases.

# The first line of input contains a single integer 𝑇 (1≤𝑇≤103), the number of test cases.

# Each of the 𝑇 following lines contains three space-separated integers 𝑎, 𝑏, and 𝑛 (0≤𝑎,𝑏,𝑛≤109) respectively.

# Output
# For each test case, output 𝑓(𝑛).

# Example
# inputCopy
# 3
# 3 4 2
# 4 5 0
# 325 265 1231232
# outputCopy
# 7
# 4
# 76
# Note
# In the first example, 𝑓(2)=𝑓(0)⊕𝑓(1)=3⊕4=7.



# THIS  TLED !!!! The input is TOO  BIG (10^9) TO DO O(N) solution 

def xornachi(a,b,c):
    prevprev = a
    prev = b
    if c == 0:
        return prevprev
    elif c == 1:
        return  prev
    else:
        for i in range(2,c+1):
            temp = prevprev ^ prev
            prevprev = prev
            prev = temp
    return temp
print(xornachi(3,4,2))
print(xornachi(4,5,0))
print(xornachi(325,265,1231232))

# THIS  TLED !!!! The input is TOO  BIG (10^9) TO DO O(N) solution 

def test(a,b,c):
    if c == 0:
        return a
    if c == 1:
        return b
    return test(a,b,c-2) ^ test(a,b,c-1)
print(test(3,4,2))
print(test(4,5,0))
# print(test(325,265,1231232))

'''
input
3
3 4 2
4 5 0
325 265 1231232

output
7
4
76
'''

# THIS  TLED !!!! The input is TOO  BIG (10^9) TO DO O(N) solution 

import sys

def xornachi(a,b,c):
    prevprev = a
    prev = b
    if c == 0:
        return prevprev
    elif c == 1:
        return  prev
    else:
        for i in range(2,c+1):
            temp = prevprev ^ prev
            prevprev = prev
            prev = temp
    return temp

tests = sys.stdin.readlines()
for line in tests[1:]:
    a, b, c = [int(elem) for elem in line.split(' ')]
    print(xornachi(a, b, c))
    
'''
3
3 4 2
4 5 0
325 265 1231232
'''



'''

n=0        0          
n=1        1          
n=2       10          
n=3       11          
n=4      100          
n=5      101          
n=6      110          
n=7      111          
n=8     1000          
n=9     1001          
n=10    1010          
'''

import sys

'''
3
11
4
100

011 xor 100
(0, 1), (1, 0), (1, 0)
'''


# THIS SOLUTION  WORKS !!!! 

# Time: O(logA+logB)
# Space: O(logA+logB) 

def xornachi(a,b,c):
    if c < 1:
        return a
    elif c == 1:
        return b

    bit_tuples = []
    while a > 0 or b > 0:
        bit_tuples.append((a&1, b&1))
        a >>= 1
        b >>= 1
    
    c_bits = []
    for a_bit,  b_bit in bit_tuples:
        c_bit = 0
        if (a_bit, b_bit) == (0, 0):
            pass
        elif (a_bit, b_bit) == (0, 1):
            # pattern is 1->0->1
            if c % 3 == 2:
                c_bit = 1
            elif c % 3 == 0:
                c_bit = 0
            else:
                c_bit = 1
        elif (a_bit, b_bit) == (1, 0):
            # pattern is 1->1->0
            if c % 3 == 2:
                c_bit = 1
            elif c % 3 == 0:
                c_bit = 1
            else:
                c_bit = 0
        elif (a_bit, b_bit) == (1, 1):
            # pattern is 0->1->1
            if c % 3 == 2:
                c_bit = 0
            elif c % 3 == 0:
                c_bit = 1
            else:
                c_bit = 1
        else:
            # this shouldn't happen
            assert False
        c_bits.append(c_bit)
        
    ans = 0
    for i, c_bit in enumerate(c_bits):
        ans += c_bit << i
    return ans

tests = sys.stdin.readlines()
for line in tests[1:]:
    a, b, c = [int(elem) for elem in line.split(' ')]
    print(xornachi(a, b, c))
    

# EYEOPEINING SOLUTION 

def test(a,b,n):
    return [a,b,a^b][n%3]
print(test(3,4,2))
print(test(4,5,0))
print(test(325,265,1231232))

