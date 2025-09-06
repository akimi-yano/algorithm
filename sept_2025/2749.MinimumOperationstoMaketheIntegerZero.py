'''
2749. Minimum Operations to Make the Integer Zero
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers num1 and num2.

In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

If it is impossible to make num1 equal to 0, return -1.

 

Example 1:

Input: num1 = 3, num2 = -2
Output: 3
Explanation: We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 22 + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 22 + (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 20 + (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
Example 2:

Input: num1 = 5, num2 = 7
Output: -1
Explanation: It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
 

Constraints:

1 <= num1 <= 109
-109 <= num2 <= 109
'''

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        '''
        num1 - (num2 + 2^i_1) - (num2 + 2^i_2) - ... - (num2 + 2^i_k) = 0
        num1 - k * num2 = 2^i_1 + 2^i_2 + ... + 2^i_k
        num1 - k * num2 という値を、ちょうど k 個の「2のべき乗」の足し算で表現できるような、最小の k を見つける
        
        3 conditions:
        1) target >= 0
        2のべき乗は必ず正の数なので、それらを足し合わせた target も0以上でなければなりません。
        
        2) target.bit_count() <= k
        bit_count() は、数値を2進数で表したときの 1 の個数を数えるメソッドです。（例: 13 は2進数で 1101 なので、13.bit_count() は 3 です）
        この 1 の個数は、その数値を表すのに最低限必要な2のべき乗の個数を意味します。
        例えば、13 = 8 + 4 + 1 であり、最低3個の2のべき乗が必要です。
        したがって、操作回数 k は、この最低必要個数以上でなければなりません。
        
        3) k <= target
        k 個の2のべき乗の和で target を作るとき、最も小さい値になるのは 1 を k 個足す場合で、その合計は k です。
        つまり、target の値は最低でも k 以上でなければなりません。
        '''
        # kを0から60まで試す
        for k in range(61):
            # 「k個の2のべき乗の和」になるべき目標値を計算
            target = num1 - k * num2
            # targetが満たすべき3つの条件をチェック
            if target >= 0 and target.bit_count() <= k <= target:
                return k # 条件を満たす最小のkが見つかったので返す
        return -1