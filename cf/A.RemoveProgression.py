# https://codeforces.com/problemset/problem/1194/A

# A. Remove a Progression
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# You have a list of numbers from 1 to 𝑛 written from left to right on the blackboard.

# You perform an algorithm consisting of several steps (steps are 1-indexed). On the 𝑖-th step you wipe the 𝑖-th number (considering only remaining numbers). You wipe the whole number (not one digit).


# When there are less than 𝑖 numbers remaining, you stop your algorithm.

# Now you wonder: what is the value of the 𝑥-th remaining number after the algorithm is stopped?

# Input
# The first line contains one integer 𝑇 (1≤𝑇≤100) — the number of queries. The next 𝑇 lines contain queries — one per line. All queries are independent.

# Each line contains two space-separated integers 𝑛 and 𝑥 (1≤𝑥<𝑛≤109) — the length of the list and the position we wonder about. It's guaranteed that after the algorithm ends, the list will still contain at least 𝑥 numbers.

# Output
# Print 𝑇 integers (one per query) — the values of the 𝑥-th number after performing the algorithm for the corresponding queries.

# Example
# inputCopy
# 3
# 3 1
# 4 2
# 69 6

# outputCopy
# 2
# 4
# 12

def remove_progression(length, idx):
    ans = []
    for i in range(length):
        ans.append(i+1)
    # print(ans)
    
    idx2 = 0 
    while idx2<len(ans)-1:
        ans.pop(idx2)
        idx2+=1
    return ans[idx-1]

# print(remove_progression(3, 1)) # 2
# print(remove_progression(4, 2)) # 4
# print(remove_progression(69, 6)) # 12


def remove_progression2(length, idx):
    return  idx * 2

print(remove_progression2(3, 1)) # 2
print(remove_progression2(4, 2)) # 4
print(remove_progression2(69, 6)) # 12



# This solution works !!!

import sys

def remove_regression(length,x):
    return x * 2

tests = sys.stdin.readlines()
for line in tests[1:]:
    length, x = [int(elem) for elem in line.split(' ')]
    print(remove_regression(length, x))