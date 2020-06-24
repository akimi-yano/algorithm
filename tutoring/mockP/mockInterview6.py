# Arrays
#   -sort vs unsort
#     -binary search
#       -identify where target is, or neighbors
#       -sorting algorithms or identifying multiple targets
#     -k number of max / min
#       -top number of criteria + frequency
#     -top number / bottom number
#     -median mean mode
#       -stats / mathematics / partitioning
#   -in place vs creating a new Array
#   -positive, negative, odd, even
#   -changing length / fixed length
#   -nested arrays / one dimensional
#   -order - stack / queue
# Strings

# Dictionaries

# BST

# Heaps

# Graphs

# Dynamic Programming

# Binary

# Conversion

# Bitwise

# Database
#   Naive Trees
# --------------------------------------------
# all lowercase, no space, no symbols
# assume valid non None non Empty input
# all words are in the sentence
# all valid anagrams in words array

words = ["bat", "the", "tab"] 
sentence = "bat the tab"
             2   1   2   
"abt"
d = {
  "abt":2,
  "eht":1
}
for i in words:
  temp = i.sort()
  if temp in d:
    d[temp] += 1
  else:
    d[temp] = 1

splitter = sentence 
ans = 1
# Time < n^3

# this will return 4

# 1 bat the tab 
# 2 bat the bat
# 3 tab the bat
# 4 tab the tab

# Time < n^3
# 1 find what are the anagram words ? how many ? -2 
# 2 spllit the sentence and check a word one by one 
# 3 


# using the sentence provided, anagrams may only swap places with duplicates
# return the number of sentences that can be generated
# times out if you generate sentences

# Time < n^3

# space - 2
# 1 to split the sentence 
# dont generate sentences


def find_permuations(words, sentence):
  return count

# Sprinkler problem
# no zeros, no negatives
# Find minimum number of sprinklers to turn on to cover the entire array
# value of 1 covers itself and left and right neighbors
# if the sprinkler goes out of bounds that's ok
# left_bound = max(0,i - arr[i])
# right_bound = min(len(arr)-1, i + arr[i])  
# arr = [1,2,4,1,2] -> 1
# arr = [1,1,1,1,1] -> 2
# arr = [1,1,1,1,5] -> 1
# arr = [5,1,4,1,1] -> 1 (more than 1 solution just return first one or whatever)


