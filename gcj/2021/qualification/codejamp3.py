import sys

def helper(N, C):
    '''
    N = 3, C = 3
    ans = [1, 3, 2]
    '''
    ans = [i for i in range(1, N+1)]
    extra = C - (N-1)
    for i in range(N-1, -1, -1):
        j = min(i+extra, N-1)
        extra -= j - i
        while i < j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
    return ans
    
num_tests = int(next(sys.stdin))
for i in range(num_tests):
    N, C = [int(elem) for elem in next(sys.stdin).split()]
    if not N - 1 <= C <= ((N)*(N+1)/2) - 1:
        print(f'Case #{i+1}: IMPOSSIBLE')
    else:
        print(f'Case #{i+1}: {" ".join([str(elem) for elem in helper(N, C)])}')