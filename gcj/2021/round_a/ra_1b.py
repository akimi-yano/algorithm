import sys

def helper(nums):
    if not nums:
        return 0
    total = 0
    max_num  = nums[0]
    for i in range(1, len(nums)):
        cur = nums[i]
        if len(cur) > len(max_num):
            max_num = cur
            continue
        found_smaller = False
        found_larger = False
        for j in range(len(cur)):
            if max_num[j] < cur[j]:
                found_larger = True
                break
            if max_num[j] > cur[j]:
                found_smaller = True
                break
        diff = len(max_num) - len(cur)
        if found_smaller:
            max_num = cur + ('0' * (diff + 1))
            total += diff + 1
            continue
        if found_larger:
            max_num = cur + ('0' * (diff))
            total += diff
            continue
        if all(c == '9' for c in max_num[len(cur):]):
            max_num = cur + ('0' * (diff + 1))
            total += diff + 1
            continue
        extra = []
        added = False
        for c in reversed(max_num[len(cur):]):
            if added:
                extra.append(c)
            elif c == '9':
                extra.append('0')
            else:
                extra.append(str(int(c) + 1))
                added = True
        max_num = cur + ''.join(reversed(extra))
        total += len(extra)
    return total
            

num_tests = int(next(sys.stdin))
for i in range(num_tests):
    next(sys.stdin)
    arr = next(sys.stdin).strip().split()
    print(f'Case #{i+1}: {helper(arr)}')