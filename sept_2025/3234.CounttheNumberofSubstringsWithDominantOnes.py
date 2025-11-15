'''
3234. Count the Number of Substrings With Dominant Ones
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
 

Constraints:

1 <= s.length <= 4 * 104
s consists only of characters '0' and '1'.
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s) # 文字列の長さ
        
        # pre 配列の準備
        # pre[i+1] (s[i]に対応) には、0-based の「ジャンプ先」インデックスを格納します。
        # このインデックス j は、s[i] が属する「1の連続ブロック」の開始位置 (j)、
        # または s[i-1] が '0' だった場合は i (j=i) を指します。
        # これにより、j = pre[j] とジャンプすることで、「0」が現れる前のブロックの先頭に
        # 効率よく移動できます。
        pre = [-1] * (N + 1)
        for i in range(N): # i は 0-based のインデックス
            if i == 0 or s[i-1] == '0':
                # i=0 の場合、または s[i-1] が '0' (ブロックの区切り) の場合
                pre[i+1] = i # s[i] 自身 (0-based) をジャンプ先として格納
            else:
                # s[i-1] が '1' (前のブロックが続いている) の場合
                pre[i+1] = pre[i] # 前のジャンプ先 (ブロックの開始位置) を引き継ぐ
        
        res = 0 # 条件を満たす部分文字列の総数
        
        # i を部分文字列の「終了位置」 (1-based) としてループ
        # (s[...i-1] を処理する)
        for i in range(1, N+1):
            
            # s[i-1] は現在の末尾文字
            # まず、現在の末尾文字 s[i-1] のみで C0 を初期化する
            cnt0 = 1 if s[i - 1] == '0' else 0
            
            # j は部分文字列の「開始位置」 (1-based)
            # j = i から開始し、pre 配列を使って左 (過去) へジャンプしていく
            j = i
            
            # j > 0 (j が有効) かつ
            # cnt0*cnt0 <= N (最適化: C0が大きすぎると C1 (最大N) を超えるため)
            while j > 0 and cnt0 * cnt0 <= N:
                
                # 現在のブロック (s[pre[j] ... i-1]) の '1' の数を計算する
                # i (1-based) - pre[j] (0-based) = ブロックの長さ
                # cnt0 = このブロック内の '0' の数 (ジャンプするたびに増える)
                cnt1 = (i - pre[j]) - cnt0
                
                # 条件 (C0^2 <= C1) を満たすかチェック
                if cnt0 * cnt0 <= cnt1:
                    # 条件を満たす場合、このブロック内で有効な「開始位置」の数を加算する
                    
                    # 候補となる開始位置の数: (j - pre[j])
                    # (現在のブロック s[pre[j] ... j-1] の長さ)
                    
                    # C1 を C0^2 以上に保つために、先頭から削除できる '1' の数:
                    # (cnt1 - cnt0 * cnt0 + 1)
                    
                    # 両方のうち、小さい方 (より厳しい制約) を加算する
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                
                # j を前のブロックの開始位置へジャンプさせる
                # j (1-based) で pre[j] を参照し、
                # pre[j] (0-based) が次の j (0-based) となる
                # (次回の while (j > 0) の評価で 0-based でも正しく機能する)
                j = pre[j]
                
                # ブロックを1つ遡った (pre[j] の位置にある '0' を越えた) ため、
                # '0' のカウントを 1 増やす
                cnt0 += 1
                
        return res