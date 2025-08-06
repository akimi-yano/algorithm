'''
3479. Fruits Into Baskets III
Medium
Topics
premium lock icon
Companies
Hint
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

 

Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
'''

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        '''
        Sqrt Decomposition. 
        Create sqrt(n) buckets of size sqrt(n) each, 
        with elements like (basket_size, basket_idx). 
        Sort the buckets prior to processing the fruits, 
        so that the max size basket is always the last element. 
        Scan through the buckets from left to right to find the first bucket that has max_basket_size >= fruit_quantity. 
        Then scan through this bucket to find and remove the smallest index which has basket_size >= fruit_quantity.

        Complexity
        Time complexity: O(nsqrtn)
        Space complexity: O(n)
        '''
        n = len(fruits)

        # sqrt decomposition
        bucket_sz = int(ceil(sqrt(n)))

        # idx -> baskets within [idx*bucket_sz, (idx+1)*bucket_sz)
        buckets = [[] for _ in range(bucket_sz)]

        for i,basket in enumerate(baskets):
            bucket_idx = i // bucket_sz
            buckets[bucket_idx].append((basket, i))

        # sort each bucket, so that the last element is always the largest basket
        for bucket in buckets:
            bucket.sort()

        # assign fruits to baskets
        ret = 0
        
        for cnt in fruits:
            for bucket in buckets:
                # bucket contains a basket that can fit our fruit
                if bucket and bucket[-1][0] >= cnt:
                    # find lowest index basket which can fit our fruit
                    chosen = min((i, basket) for basket,i in bucket if basket >= cnt)
                    bucket.remove((chosen[1], chosen[0]))
                    break
            else:
                ret += 1

        return ret