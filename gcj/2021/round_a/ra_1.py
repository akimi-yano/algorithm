import sys

def helper(nums):
    if not nums:
        return 0
    total = 0
    max_num  = nums[0]
    for i in range(1, len(nums)):
        cur = nums[i]
        if cur > max_num:
            max_num = cur
            continue
        if cur == max_num:
            max_num *= 10
            total += 1
            continue
        extra_digits = len(str(max_num)) - len(str(cur))
        # 111
        #  10
        if (max_num // (10**extra_digits)) > cur:
            max_num = cur * (10**(extra_digits+1))
            total += extra_digits + 1
        # 111
        #  12
        elif (max_num // (10**extra_digits)) < cur:
            max_num = cur * (10**(extra_digits))
            total += extra_digits
        # 1119
        # 111
        else:
            leftover = max_num - (cur*(10**(extra_digits)))
            if len(str(leftover)) < len(str(leftover+1)):
                max_num = cur * (10**(extra_digits+1))
                total += extra_digits + 1
            else:
                leftover += 1
                max_num = cur * (10**(extra_digits)) + leftover
                total += extra_digits
    return total
            

num_tests = int(next(sys.stdin))
for i in range(num_tests):
    next(sys.stdin)
    arr = [int(elem) for elem in next(sys.stdin).strip().split()]
    print(f'Case #{i+1}: {helper(arr)}')