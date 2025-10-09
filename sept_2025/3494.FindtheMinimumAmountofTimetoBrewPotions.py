'''
3494. Find the Minimum Amount of Time to Brew Potions
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	0	5	30	40	60
1	52	53	58	60	64
2	54	58	78	86	102
3	86	88	98	102	110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
 
'''

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        '''
        FORWARD PASS:
        魔法使い自身が手が空いていること: i番目の魔法使いが、1つ前のポーション(j-1)の作業を終えている必要があります。この時刻が done[i+1] に記録されています。
        ポーションが流れてきていること: i-1番目の魔法使いが、今まさに扱っているポーション(j)の作業を終えて、渡してくれる必要があります。この時刻が done[i] です。
        したがって、作業を開始できるのは、この2つの時刻のうち 遅い方 (max(done[i+1], done[i])) です。

        BACKWARD PASS:
        完了時刻から作業時間を引き算して、開始時刻を逆算する という処理をしています。

        一言でいうと、「ある魔法使いの『作業開始時刻』は、その一つ前の魔法使いの『作業完了時刻』と全く同じはずだ」という考え方に基づいています。
        '''
        N, M = len(skill), len(mana)
        done = [0] * (N+1)

        for j in range(M):
            # ensure wizard i+1 starts only when both the previous wizard and potion are ready.
            for i in range(N):
                done[i+1] = max(done[i+1], done[i]) + mana[j] * skill[i]
            
            # adjust backward to synchronize potion passing between wizards.
            for i in range(N-1, 0, -1):
                done[i] = done[i+1] - mana[j] * skill[i]
        
        return done[N]