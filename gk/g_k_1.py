import sys

def helper(string):
    if not string:
        return ""

    ans = ["1"]
    start = 0
    for i in range(1, len(string)):
        if string[i-1] >= string[i]:
            start = i
        ans.append(str(i - start+1))

    return " ".join(ans)
    
num_tests = int(next(sys.stdin))
for i in range(num_tests):
    next(sys.stdin)
    string = next(sys.stdin).strip()
    print(f'Case #{i+1}: {helper(string)}')