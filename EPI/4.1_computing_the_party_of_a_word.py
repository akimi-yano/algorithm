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
def single_word(s):
    counter = 0
    for c in s:
        if c=="1":
            counter+=1
    if counter%2==0:
        return 0
    else:
        return 1
print(single_word("1011"))
print(single_word("10001000"))

def many_words(arr):
    count_0=0
    count_1=0
    for s in arr:
        ans = single_word(s)
        if ans == 0:
            count_0+=1
        else:
            count_1+=1
    if count_1%2==0:
        return 0
    else:
        return 1
print(many_words(["1011","1011","1011"]))