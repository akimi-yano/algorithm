# [Completed]
# 4.1 computing the party of a word
# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
# example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
# single bit errors in data storage and communication. It is fairly straightforward to write code that
# computes the parity of a single 64-bit word.
# How would you compute the parity of a very large number of 64-bit words?


# * parity == (量・質・価値など)同等であること，等価
# odd # of 1s -> parity - 1
# even # of 1s -> parity - 0 

# "1011" -> 1
# "10001000" -> 0
# then
# "1011","1011","1011" ... ?


def parity(x):
    print("performing ", bin(x), " XOR ", bin(x>>32))
    
    print(bin(x))
    x = x ^ (x >> 32)
    print(bin(x))
    x ^= x >> 16
    print(bin(x))
    x ^= x >> 8
    print(bin(x))
    x ^= x >> 4
    print(bin(x))
    x ^= x >> 2
    print(bin(x))
    x ^= x >> 1

    print(bin(x), bin(1))
    x &= 1
    print(bin(x))
    return x

num1 = int('1111111111111111111111111111111100000000000000000000000000000001', base=2)
num2 = int('1111111111111111111111111111111100000000000000000000000000000000', base=2)

print("ANSWER: ",parity(num1))
print("*"*100)
print("ANSWER: ",parity(num2))