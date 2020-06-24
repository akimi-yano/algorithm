'''
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list 
of non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in 
the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as 
"leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented 
as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


memo ----
space- separeated : if I can use a word from dictionary
s is not empty
"" in dictionary

no dup in dictionary

input: string and [string] 

output: boolean

"cats and |og"

"cats", X
"dog",  X
"sand", X
"and", 
"cat"]

cats + and  =---> |og cache[0][6] ---> catsand: True


cat + sand.  ---->  no need to look


plan - turn the dictionary array to set 
iterate through the set to check each word
slice the string and make a substring and check if it 
matches with the word in the set of word dict

base- sub string is empty - ive checked all the words - > true
if something is left after the iteration then false 

recursive- (call it if the substring is in the dictionary)
pass in the rest of the sub / string


-> check if i can make it more efficient



memorization:
key: cats catsand,
key: [0,3], i,j
w_dict = {'cats': True, catsand: True}
w_dict = {(0,3): True, (0,6): True}

tabulation 2D
cache[0][3] = True, 
dp[i][j].  ---> i = 0, j  i is always 0

tabaulation 1D
dp[j]  = True


cache_dict = {key:value}


'''
# slicing solution + memolization
def word_dict(s, wordDict):
  word_set = set(wordDict)
  memo = {}
  def helper(sub):
    if sub in memo:
      return memo[sub]
    if not sub:
      return True
    for word in word_set:
      if sub[:len(word)] != word:
        continue
      if helper(sub[len(word):]):
        memo[sub] = True
        return True
    memo[sub] = False
    return False
  return helper(s)
print("slicing+memo: ",word_dict("leetcode",["leet", "code"])) #should return True
print("slicing+memo: ",word_dict("applepenapple",["apple", "pen"])) #should return True
print("slicing+memo: ",word_dict("catsandog",["cats", "dog", "sand", "and", "cat"])) #should return False



# index solution + memolization
def word_dict_idx(s, wordDict):
  word_set = set(wordDict)
  memo = {}
  def helper(i,j):
    if (i,j) in memo:
      return memo[(i,j)]
    if i>len(s)-1 or j>len(s)-1:
      return True
    for word in word_set:
      j=i+len(word)
      # print(s[i:j])
      if s[i:j] != word:
        continue
      if helper(j,j):
        memo[(i,j)]=True
        return True
    memo[(i,j)]=False
    return False
  return helper(0,0)
print("indexing+memo: ",word_dict_idx("leetcode",["leet", "code"])) #should return True
print("indexing+memo: ",word_dict_idx("applepenapple",["apple", "pen"])) #should return True
print("indexing+memo: ",word_dict_idx("catsandog",["cats", "dog", "sand", "and", "cat"])) #should return False

'''
01234567  
leetcode

leet 0,3
code 4,7

'''

# tabulation solution
def word_dict_tab(s, wordDict):
  word_set = set(wordDict)
  tab = [0]*(len(s)+1)
  tab[0]=1
  # print(tab)
  for j in range(1,len(s)+1):
    for i in range(j):
      if tab[i] == 1 and s[i:j] in word_set:
        tab[j] = 1
        break
      else:
        tab[j] = 0 
  # print(tab)
  return tab[-1] == 1

  
print("tabulation: ",word_dict_tab("leetcode",["leet", "code"])) #should return True
print("tabulation: ",word_dict_tab("applepenapple",["apple", "pen"])) #should return True
print("tabulation: ",word_dict_tab("catsandog",["cats", "dog", "sand", "and", "cat"])) #should return False

