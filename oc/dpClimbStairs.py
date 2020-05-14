# climb staris
# if n == 6 should return 24

# regular recursion - slow
# Time O(3^N) - exponential - because for every recursive call, we're making three more calls
def climb_stairs(n):
    def climb(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        return climb(n-1)+climb(n-2)+climb(n-3)
    return climb(n)
    
print(climb_stairs(6))


# DP & memorization - faster than the normal recursion
# Time O(3N) - linear - because we make N calls, and for each of those calls, make 3 calls 
def climb_stairs_memo(n):
    cache = {}
    def climb(n):  
        if n in cache:
            return cache[n]
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        cache[n] = climb(n-1)+climb(n-2)+climb(n-3)
        return cache[n]
    return climb(n)
print(climb_stairs_memo(6))


# now fox can jump, 2,3,or 5 step at a time
# n = number of staris
# jumps = array of options for jumps ex[2,3,5]
# Time O(N*K^2) where N is destination (# of steps to climb) and K is length of jumps array
def climb_stairs_tab(n, jumps):
    # innitialize an array with (n+1) elements (each element to be innitialized as 0)
    steps = [0]*(n+1)
    #first step is innevitable and only 1 possibility of not climbing 
    steps[0] = 1
    #iterate the jump array
    for j in range(len(jumps)):
        for step in range(jumps[j], len(steps)):
            step_sum = 0
            for k in range(j+1):
                step_sum += steps[step-jumps[k]]
            steps[step] = step_sum
    return steps[n]    
print(climb_stairs_tab(10,[2,3,5]))