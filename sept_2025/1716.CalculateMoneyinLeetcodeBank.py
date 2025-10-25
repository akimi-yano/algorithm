'''
1716. Calculate Money in Leetcode Bank
Solved
Easy
Topics
premium lock icon
Companies
Hint
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        # 1. 週の数と残りの日数を計算
        weeks, days = divmod(n, 7)
        
        # 2. 合計金額を計算：　「完了した週の合計」と「最後の残りの日数の合計」
        weekly_basic_amount = 28 # (1+2+3+4+5+6+7) = $28
        basic_amount_of_all_weeks = weeks * weekly_basic_amount
        weekly_additional_amount = (weeks*(weeks-1)//2)*7 # 1st week: +$0, 2nd week: +$7, 3rd week: +$14 -> $7 * (0+1+2+...) so use k*(k+1)//2*7

        # weeks 週間が完了した後、次の週（最後の不完全な週）は weeks + 1 ドルからスタートします。
        # この最後の週の days 日間の貯金額は、以下のようになります。
        # (weeks + 1) + (weeks + 2) + ... + (weeks + days)
        # この数式は、2つの部分に分解できます。
            # (weeks + weeks + ... + weeks) (←days 回) : weeks*days: weeks を days 回足したものです。
            # + (1 + 2 + ... + days) : (days*(days+1)//2): 1 から days までの合計です。
        remaining_days = weeks*days + (days*(days+1)//2)

        total_amount = basic_amount_of_all_weeks + weekly_additional_amount + remaining_days
        
        # 3. 合計を返す
        return total_amount