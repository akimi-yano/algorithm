import sys
from functools import lru_cache

primes = None

@lru_cache(None)
def helper(i, add_left, mult_left):
    # print(i, add_left, mult_left)
    if i >= len(primes):
        return add_left == 0 and mult_left == 1
    if add_left < 0:
        return False
    num = primes[i]
    if mult_left % num:
        return helper(i+1, add_left - num, mult_left)
    return helper(i+1, add_left - num, mult_left) or helper(i+1, add_left, mult_left // num)

    
num_tests = int(next(sys.stdin))
for i in range(num_tests):
    num_primes = int(next(sys.stdin))
    primes = []
    while num_primes:
        num, q = next(sys.stdin).strip().split()
        for _ in range(int(q)):
            primes.append(int(num))
        num_primes -= 1
        
    for total in range(sum(primes), 0, -1):
        if helper(0, total, total):
            print(f'Case #{i+1}: {total}')
            break
    else:
            print(f'Case #{i+1}: 0')
    helper.cache_clear()