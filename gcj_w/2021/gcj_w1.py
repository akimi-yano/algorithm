import sys
from collections import Counter
def helper(arr):
    counts = Counter(arr)
    c = 1
    ans = 0
    for q in counts.values():
        ans += c * q
        c += 1
    return ans
    
num_tests = int(next(sys.stdin))
for i in range(num_tests):
    next(sys.stdin)
    arr = [int(elem) for elem in next(sys.stdin).strip().split()]
    print(f'Case #{i+1}: {helper(arr)}')

