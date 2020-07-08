# 698. Partition to K Equal Sum Subsets

# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array 
# into k non-empty subsets whose sums are all equal.

# Example 1:

# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.


# TLEed with this solution ..... nooo

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        total = sum(nums)
        if total%k !=0:
            return False
        each = total/k
 
        def helper(start,used,num_parts,target_sum,progress_sum):
            if num_parts == 1:
                return True
            if progress_sum == target_sum:
                return helper(0,used,num_parts-1,target_sum,0)
            for i in range(start,len(nums)):
                if used[i] == 0:
                    used[i]=True
                    if helper(start+1,used,num_parts,target_sum,progress_sum+nums[i]):
                        return True
                    used[i]=False
            return False
                
        return helper(0,[0]*len(nums),k,each,0)
        

# and this works - optimized ver

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k==1: return True

        self.n=len(nums)
        if k>self.n: return False

        total=sum(nums)
        if total%k: return False

        self.target=total/k
        visit=[0]*self.n

        nums.sort(reverse=True)
        def dfs(k,ind,sum):
            if k==1: return True
            if sum==self.target:
                return dfs(k-1,0,0)
            for i in range(ind,self.n):
                if not visit[i] and sum+nums[i]<=self.target:
                    visit[i]=1
                    if dfs(k,i+1,sum+nums[i]): 
                        return True
                    visit[i]=0
            return False

        return dfs(k,0,0)
        
      