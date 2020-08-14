# 49. Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


# Yay this works ! there might be more efficient way to do this ! 

'''
        groups:
        1 aet
        2 ant
        3 abt
        
        ["eat", "tea", "tan", "ate", "nat", "bat"]
        sorted:[original]
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            sorted_list = sorted(s)
            sorted_str = "".join(sorted_list)
            if sorted_str not in memo:
                memo[sorted_str]=[s]
            else:
                memo[sorted_str].append(s)
        return memo.values()
        


# different ways to solve this problem:

'''
Python solution 1

Sort and group by group identifier, then sort each group normally.

'''

def groupAnagrams(self, strs):
    return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]
'''
Or "breaking it down" to maybe make it more readable for beginners and because I just noticed that in Firefox 
it violates my self-imposed "no scrollbars" rule (I usually use Chrome and didn't think it differed):
'''

def groupAnagrams(self, strs):
    groups = itertools.groupby(sorted(strs, key=sorted), sorted)
    return [sorted(members) for _, members in groups]
'''
Python solution 2

Using defaultdict to collect the groups.
'''

def groupAnagrams(self, strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return map(sorted, groups.values())


def anagrams(self, strs):
    count = collections.Counter([tuple(sorted(s)) for s in strs])
    return filter(lambda x: count[tuple(sorted(x))]>1, strs)
'''
collections.Counter creates a counter object. 
A counter object is like a specific kind of dictionary where it is build for counting (objects that hashes to same value)
tuple(sorted(s)) is used here so that anagrams will be hashed to the same value. 
tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
lambda function defined here returns True if number of anagrams of that elements is greater than 1
'''


def groupAnagrams(self, strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()