def longest_flat(array):
    max_len = 0
    start = 0
    end = 0
    while end<len(array):
        counter = 0
        while end<len(array) and array[start]==array[end]:
            counter +=1
            end+=1
        max_len=max(max_len,counter)
        start+=1
    return max_len
            
# print(longest_flat([1,1,1]))
print(longest_flat([]))
print(longest_flat([2]))

# The deletion distance between two strings is the minimum number of characters that you need to delete in the two strings 
# in order to have the same string. The deletion distance between cat and at is 1, because you can just delete the first 
# character of cat. The deletion distance between cat and bat is 2, because you need to delete the first character of both words. 
# Of course, the deletion distance between two strings can't be greater than the sum of their lengths, 
# because you can always just delete both of the strings entirely.Implement an efficient function to find the deletion distance 
# between two strings.You can refer to the Wikipedia article on the algorithm for edit distance if you want to. 
# The algorithm there is not quite the same as the algorithm required here, but it involves similar ideas.

def deletion_distance(str1, str2):
    if len(str1) < 1:
        return len(str2)
    if len(str2) < 1:
        return len(str1)
    best = 1 + min(
        deletion_distance(str1, str2[1:]),
        deletion_distance(str1[1:], str2))
    if str1[0] == str2[0]:
        best = min(
            best,
            deletion_distance(str1[1:], str2[1:]))
    return best



# A string of brackets is correctly matched if you can pair every opening bracket up with a later closing bracket, 
# and vice versa. For example, (()()) is correctly matched, and (() and )( are not.Implement a function which takes a 
# string of brackets and returns the minimum number of brackets you'd have to add to the string to make it correctly matched.
# For example, (() could be correctly matched by adding a single closing bracket at the end, so you'd return 1. )( can be 
# correctly matched by adding an opening bracket at the start and a closing bracket at the end, so you'd return 
# 2.If your string is already correctly matched, you can just return 0.
def bracket_match(bracket_string):
    count = 0
    for elem in bracket_string:
        if elem == '(':
            count += 1
        else:
            count -= 1
    return abs(count)

# Write a function that takes a list of daily stock prices (the price of one stock measured once a day for N days) and 
# returns the length of the longest number of days over which the price of the stock continually rose or continually fell 
# (strictly rose or strictly fell).