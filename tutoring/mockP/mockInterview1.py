# given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
# it is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# words in the list of banned words are given in lowercase, and free of punctuation.  
# words in the paragraph are not case sensitive.  
# the answer is in lowercase.
 
# input: 
# paragraph = "bob hit a ball, the hit ball flew far after it was hit."
# banned = ["hit"]
# output: "ball"
 
# example of regex:
# string = "hello akimi."
# string = re.sub("[,.?!;]", ' ', string)
# string is now h llo
 

# a = remove_punctuation(str)
# memo  = {}
# paragraph  - turn it into all lower case, .split( )
# banned -> set - continue 

# in memo -> +=1

# best = 0
# ans = “”
# for k, v in memo.items():

# if v > best
# best = v
# ans = k

# return ans 





def find_most_frequent(para, banned):
para = remove_punctutations(para)
para = para.lower()
para_list = para.split( )
memo = {}
banned_set = set(banned)
for word in para_list:
	if word not in banned_set:
			if word not in memo:
				memo[word]= 1
			else:
				memo[word]+=1
	ans = “”
	best = 0
	for k, v in memo.items():
		if v>best:
best = v
ans = k

return ans 





# // input vs output
# // data, constraints -> 
# // frequency -> max heap / min heap
# // data structure // implementation // usage
# // ((“word”, count))


# adjacency list = {
# 	“key” : [1,2,3]
# }







# in a town, there are n people labelled from 1 to n.  there is a rumor that one of these people is secretly the celebrity.
# if the celebrity exists, then:
# the celebrity likes nobody.
# everybody (except for the celebrity) likes the celebrity
# there is exactly one person that satisfies properties 1 and 2.
# you are given likes, an array of pairs likes[i] = [a, b] representing that the person labelled a likes the person labelled b.
# if the celebrity exists and can be identified, return the label of the celebrity.
# assume always 1 celebrity
# add case where there is no celebrity
# likes = [[‘A’,’B’],[‘B’,’C’],[‘A’,’C’]]
# Number = 3
# Output -> ‘C’
# Adjacency_list = {
# 	“A”:[],
# “B”:[A],
# “C”:[B,A]
# }


# 1 c

# 1 c -> no one  = if c, c not in [0] of each arr
# 2 e -> c = if c, c in [1] of everyone but c 

# input = [[int ]]
# Output 

def findCelebrity(likes, number):
	adjecency_list = {}
	for i in range(len(likes)):
		if likes[i][1] not in adjecency_list:
			adjecency_list[likes[i][1]] = set([likes[i][0]])
        else:
            adjecency_list[likes[i][1]].add(likes[i][0])
	
for k,v in adjacency_list.items():
	if len(v) == number -1:
	candidate = key
for k, v in  adjacency_list.items():
	if candidate in v:
 	return -1
return candidate
# ---------------
# Djikstra

# Weighted graphs / unweighted graphs
# Graph with weights, and each node represents a city with a satisfaction value
# Each weighted path represents the amount of time to travel to a city
# Find the optimal path in terms of highest satisfaction if you had 1 hour to travel

# Atlassian -> 
# Palantir -> Cryptography




# DFS / BFS / A* /  Kmeans

# Optimal pathing in matrices - BFS
# ---------------------------------------
# Looking for depth of a tree
# Counting number of islands
# BST - inorder, preorder , postorder
# Helper ( node ) {
# 	If node == null {
# 		Return 
# }	
# console.log(‘preorder’)
# helper(node.left)
# console.log(‘inorder’)
# helper(node.right)
# console.log(‘postorder’)
# }

# [
# [O , O , O , X]
# [O , X , O , X]
# [O , X , O , O]
# [O , X , O , O]
# ]
