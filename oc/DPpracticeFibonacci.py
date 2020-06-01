# DP practice session with fibonacci

def fib(n):
    memo ={}
    def helper(n):
        if n in memo:
            return memo[n]
        if n<2:
            return n
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    return helper(n)
print(fib(20))


def tabfib(n):
    table = [0 for _ in range(n+1)]
    table[0]=0
    table[1]=1
    for i in range(2,len(table)):
        table[i]=table[i-1]+table[i-2]
    print(table)
    return table[n]
print(tabfib(20))