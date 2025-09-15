'''
3685. Subsequence Sum After Capping Elements
Attempted
Medium
premium lock icon
Companies
Hint
You are given an integer array nums of size n and a positive integer k.

An array capped by value x is obtained by replacing every element nums[i] with min(nums[i], x).

For each integer x from 1 to n, determine whether it is possible to choose a subsequence from the array capped by x such that the sum of the chosen elements is exactly k.

Return a 0-indexed boolean array answer of size n, where answer[i] is true if it is possible when using x = i + 1, and false otherwise.

 

Example 1:

Input: nums = [4,3,2,4], k = 5

Output: [false,false,true,true]

Explanation:

For x = 1, the capped array is [1, 1, 1, 1]. Possible sums are 1, 2, 3, 4, so it is impossible to form a sum of 5.
For x = 2, the capped array is [2, 2, 2, 2]. Possible sums are 2, 4, 6, 8, so it is impossible to form a sum of 5.
For x = 3, the capped array is [3, 3, 2, 3]. A subsequence [2, 3] sums to 5, so it is possible.
For x = 4, the capped array is [4, 3, 2, 4]. A subsequence [3, 2] sums to 5, so it is possible.
Example 2:

Input: nums = [1,2,3,4,5], k = 3

Output: [true,true,true,true,true]

Explanation:

For every value of x, it is always possible to select a subsequence from the capped array that sums exactly to 3.

 

Constraints:

1 <= n == nums.length <= 4000
1 <= nums[i] <= n
1 <= k <= 4000
 
'''

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        # 1. 準備
        nums.sort() # Aを昇順にソート。小さい数字から効率的に扱うため。
        n = len(nums)
        res = [False] * n # n個のFalseで満たされた結果リストを初期化

        # dpは「作れる合計金額」を記録するビットマスク。
        # dp = 1 は 2^0 なので、「合計0が作れる」状態からスタート。
        dp = 1 
        
        # kを超える合計は不要なので、(k+1)ビットより上を0にするためのマスク
        mask = (1 << k + 1) - 1 
        
        i = 0 # ソート済みリストAのどこまで見たかを示すインデックス

        # 2. メインループ (x=1からnまで試す)
        for x in range(1, n + 1):
            # 3. DPテーブルの更新
            # Aの中に現在のx以下の数字があれば、それらを使って作れる合計金額の
            # パターンをdpに記録していく。
            while i < n and nums[i] <= x:
                # dp << A[i]: 今まで作れた合計金額すべてにA[i]を加算する操作
                # dp |= ... : 新しく作れるようになった合計金額のパターンを現在のdpに追加
                dp |= (dp << nums[i]) & mask
                i += 1

            # 4. 判定
            # ここからがこのコードの核心部分。
            # 目標kを達成するには、(x以下の数字で作った合計j) + (xより大きい数字で作った合計) = k
            # となれば良い。「xより大きい数字」はすべてxとして扱われるので、
            # その合計は m * x (mは使う個数) となる。
            # つまり、 k - j = m * x となれば良い。これは (k - j) が x の倍数であること、
            # すなわち k % x == j % x と同義。
            
            # 探すべき合計jの最小値を計算
            # jは k - (残りの要素数) * x 以上である必要がある。
            # また、jの剰余は k % x でなければならない。
            v = max(k % x, k - (n - i) * x)

            # vからkまで、x刻みでループ。これにより j % x == k % x を満たすjだけをチェックできる
            for j in range(v, k + 1, x):
                # dp & (1 << j) は、dpのjビット目が1か(合計jが作れるか)をチェック
                if dp & (1 << j):
                    # 条件を満たすjが見つかったので、このxではkを達成可能
                    res[x - 1] = True
                    break # 次のxのチェックに移る
        
        return res

# Anther way:

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        # 1. 準備
        nums.sort()
        n = len(nums)
        res = [False] * n

        # 以前のコード: dp = 1 (ビットマスク)
        #
        # 新しいコード: dp = [True, False, False, ...] (配列)
        # dp[j] が True なら「合計 j が作れる」ことを示す。
        # サイズは k+1 (0からkまで)。
        dp = [False] * (k + 1)
        dp[0] = True  # 合計0は何も選ばなければ常に作れる

        i = 0  # ソート済みリストAのどこまで見たかを示すインデックス

        # 2. メインループ (x=1からnまで試す)
        for x in range(1, n + 1):
            # 3. DPテーブルの更新 (ここが分かりやすくなった部分！)
            # Aの中に現在のx以下の数字があれば、それを使って作れる合計をdpに反映
            while i < n and nums[i] <= x:
                num = nums[i] # 新しく使えるようになった数字

                # 以前のコード: dp |= (dp << num) & mask
                #
                # 新しいコード: ループでdp配列を更新
                # kからnumに向かって逆順にループすることがポイント。
                # (順方向にループすると、同じnumを1ステップ内で複数回使ってしまうため)
                for current_sum in range(k, num - 1, -1):
                    # もし「current_sum - num」という合計が既に作れるなら...
                    if dp[current_sum - num]:
                        # ...それにnumを足した「current_sum」も作れるようになる
                        dp[current_sum] = True
                i += 1

            # 4. 判定 (この部分のロジックは元コードと全く同じ)
            # 「x以下の数字で作った合計j」と「xにキャップされた数字」を
            # 組み合わせて k を作れるかチェックする。
            
            remaining_elements = n - i
            
            # 探すべき合計jの最小値を計算
            min_j_needed = k - remaining_elements * x
            start_j = max(k % x, min_j_needed)

            # start_jからkまで、x刻みでループ
            for j in range(start_j, k + 1, x):
                # もし合計jが作れるなら (dp[j]がTrueなら)
                if dp[j]:
                    res[x - 1] = True # このxでは目標達成可能
                    break
        
        return res