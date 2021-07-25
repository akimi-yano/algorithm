# 1938. Maximum Genetic Difference Query
# Hard

# 137

# 7

# Add to List

# Share
# There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.

# You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.

# Return an array ans where ans[i] is the answer to the ith query.

 

# Example 1:


# Input: parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
# Output: [2,3,7]
# Explanation: The queries are processed as follows:
# - [0,2]: The node with the maximum genetic difference is 0, with a difference of 2 XOR 0 = 2.
# - [3,2]: The node with the maximum genetic difference is 1, with a difference of 2 XOR 1 = 3.
# - [2,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.
# Example 2:


# Input: parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
# Output: [6,14,7]
# Explanation: The queries are processed as follows:
# - [4,6]: The node with the maximum genetic difference is 0, with a difference of 6 XOR 0 = 6.
# - [1,15]: The node with the maximum genetic difference is 1, with a difference of 15 XOR 1 = 14.
# - [0,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.
 

# Constraints:

# 2 <= parents.length <= 105
# 0 <= parents[i] <= parents.length - 1 for every node i that is not the root.
# parents[root] == -1
# 1 <= queries.length <= 3 * 104
# 0 <= nodei <= parents.length - 1
# 0 <= vali <= 2 * 105

# This solution works:

'''
General idea is the following: we traverse our tree using dfs and each time we update our trie, where we keep binary representation of numbers. We need both to insert and to remove elements from trie, because once we finish traverse some node in dfs, we no longer need it. Here I spend some time in python to avoid TLE, and finally we have Trie class as following:

We keep embedded dictionary of dictionaries. Key -1 corresponding for frequency: we need this when we add and delete binary numbers from trie.
Also we use knowledge that all vals in queries are no bigger than 2*10^5 < 2^18. so we always will add binary numbers with leading zeroes, for example when we add 11101, we add 000000000000011101 in fact. Also we update frequencies: increase if we add and decrease if we delete.
Now, for find it is classical if you already solved 421: Each time we try to find bit such that XOR of bits is equal to 1 and go to accoridng branch of our trie. If it is not possible, we go to another branch. Note, that some frequencies can be 0, so we need to make sure that we go only if it is not zero.
Now, let us talk about original funcion:

First of all, we need to rearrange queries to defaultdict Q: where for each node we keep pair (index, value).
Also we create graph from our parents nodes.
Now, we traverse our tree, using dfs: first insert value when we first visit it, then for each pair i, val for this node update ans, run function recursively for all children and finally remove value from trie.
Complexity
Let M be maximum number of bits possible in queries. Then we have time complexity O((n+q)*M), where n is size of our tree and q is number of queries. Time complexity is O(n*M). In python however it works quite slow, even though I use ints, not strings, I was a bit suprised that it did not make my code faster, anybody have any ideas?

'''
class Trie:
    def __init__(self):
        self.root = {-1: 0}

    def insert(self, num, f):
        d = self.root
        for i in range(18, -1, -1):
            bit = (num >> i) & 1
            d = d.setdefault(bit, dict())
            d[-1] = d.get(-1, 0) + f

    def find(self, num):
        node = self.root
        res = 0
        for i in range(18, -1, -1):
            bit = (num >> i) & 1
            desired = 1-bit if 1-bit in node and node[1-bit][-1] > 0 else bit
            res += (desired ^ bit) << i
            node = node[desired]
        return res

class Solution:
    def maxGeneticDifference(self, parents, queries):
        Q, graph = defaultdict(list), defaultdict(list)
        for i, (node, val) in enumerate(queries):
            Q[node].append((i, val))
            
        for i, x in enumerate(parents):
            graph[x].append(i)
        
        ans, trie = [-1 for _ in queries], Trie()
        
        def dfs(node):
            trie.insert(node, 1)
            for i, val in Q[node]: ans[i] = trie.find(val)
            for neib in graph[node]: dfs(neib)
            trie.insert(node, -1)
                
        dfs(graph[-1][0]) 
        return ans