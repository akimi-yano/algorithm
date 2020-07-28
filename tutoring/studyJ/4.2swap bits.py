# 4.2 swap bits

# # this doesnt work
# def swap(x,i,j):
#     # print(bin(x))
#     # print(f"i: {i}")
#     # print(f"j: {j}")
#     # print(bin(11))
#     num=x
#     if i>j:
#         swap(x,j,i)
    
#     # i is smaller than j
#     t=i
#     while t:
#         num>>=1
#         t-=1
#     smaller = num&1
#     # print(num)
#     k=j-i

#     while k:
#         num>>=1
#         k-=1
#     # print(num)
#     larger = num&1
#     # print(larger,smaller)
#     if larger == smaller:
#         return x
#     else:
#         if larger:
#             x+=2**i
#             x-=2**j
#         else:
#             x-=2**i
#             x+=2**j
#         return x

# print(swap(73,1,6)) #expected 11

# # 1 check if they are different (i&j)
#     # i j
#     # 0 0
#     # 1 1
#     # 0 1 -> 
#     # 1 0 -> 
# # 2 change if so


# this works
def swap_bits(x,i,j):
    # extract the i-th and j-th bits, and see if they differ
    if (x>>i)&1 != (x>>j)&1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1 when x = 0 we can perform the flip xor
        bit_mask  = (1<<i) | (1<<j)
        x^=bit_mask
    return x        
    
print(swap_bits(73,1,6))