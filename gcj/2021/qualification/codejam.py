# import sys

# def helper(remaining, arr):
#     if arr == list(sorted(arr)):
#         return remaining
#     if remaining <= 0:
#         return float('inf')
#     min_ops = float('inf')
#     for start in range(len(arr)):
#         for end in range(start, len(arr)):
#             new_arr = arr[:start] + list(reversed(arr[start:end+1])) + arr[end+1:]
#             min_ops = min(min_ops, end-start + 1 + helper(remaining - 1, new_arr))
#     return min_ops

# input_data = sys.stdin.read().split('\n')
# num_cases = input_data[0]
# cases = input_data[1:]
# count = 1
# for i in range(0, int(num_cases)*2, 2):
#     N = int(cases[i])
#     print("array_size is", N)
#     str_arr = cases[i+1].split()
#     arr = [int(elem) for elem in str_arr]
#     print("elements are", arr)
#     num_iterations = N-1
#     ans  = helper(num_iterations, arr)
#     print(f"Case # {count}: {ans}")
#     count += 1

    

    
