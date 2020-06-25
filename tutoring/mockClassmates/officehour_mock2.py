# Valid Palindrome Removal
# Return true if the input is a palindrome, or can be a palindrome with no more than one character deletion.
# Zero characters can be added.

# Return false if the input is not a palindrome and removing any one character from it would not make it a palindrome.
# Must be done in constant space and linear time.
# Example input 1: 'bbabac'
# output: true

# Deleting either a letter b or the letter c would make this a palindrome if it were reordered correctly.
# Example input 2: 'carracers'
# output: carerac   rc  false


def is_palin(s):
  memo = {}
  for c in s:
    if c not in memo:
      memo[c]=1
    else:
      memo[c]+=1
  odd_counter = 0
  for v in memo.values():
    if v%2!=0:
      odd_counter+=1
  return odd_counter<3

print(is_palin('bbabac'))
print(is_palin('carracers'))

