'''
1128. Number of Equivalent Domino Pairs
Easy
Topics
Companies
Hint
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
'''

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        for i in range(len(dominoes)):
            count[tuple(sorted(dominoes[i]))] += 1
        ans = 0
        for v in count.values():
            if v > 1:
                ans += math.comb(v, 2)
        return ans
    
# Another way:

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        for i in range(len(dominoes)):
            count[tuple(sorted(dominoes[i]))] += 1
        ans = 0
        for v in count.values():
            # v個の要素から2つを選ぶ組み合わせの数（コンビネーション）を求める
            '''
            公式　n! // r!(n−r)! より
            v! // 2!(v−2)!  = v(v−1) // 2
​            '''
            ans += v * (v - 1) // 2
        return ans