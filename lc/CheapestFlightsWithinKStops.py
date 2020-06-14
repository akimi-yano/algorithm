# Cheapest Flights Within K Stops

# wrong ver - why ? : you should not pass in total 
# but do this
# helper(c) -> 0
# helper(b) -> 200+helper(c)
# helper(a) -> 100+helper(b)

# class Solution:
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # self.k = K
        # self.dst = dst
        # memo = {}
        # for flight in flights:
        #     if flight[0] not in memo:
        #         memo[flight[0]] = set([(flight[1],flight[2])])
        #     else:
        #         memo[flight[0]].add((flight[1],flight[2]))
        # # print(memo)
        # visited  = set([])
        # def helper(current,total,layover):
        #     # print(current, total, layover)
        #     if current == self.dst:
        #         return total
        #     # if layover >self.k:
        #     #     return math.inf
        #         # only direct flight
        #     visited.add(current)
        #     best_cost = math.inf
        #     # which ever
        #     if current in memo:
        #         for info in memo[current]:
        #             next_stop,cost = info
        #             if next_stop not in visited:
        #                 if layover<self.k or (layover==self.k and next_stop == self.dst):
        #                     best_cost=min(best_cost,helper(next_stop,total+cost,layover+1))
        #     # print(best_cost)
        #     return best_cost
        # ans = helper(src,0,0)
        # return -1 if ans == math.inf else ans
        

# correct ver
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.k = K
        self.dst = dst
        adj = {}
        for flight in flights:
            if flight[0] not in adj:
                adj[flight[0]] = set([(flight[1],flight[2])])
            else:
                adj[flight[0]].add((flight[1],flight[2]))
        # print(memo)
        memo = {}
        def helper(current,layover):
            if (current, layover) in memo:
                return memo[(current, layover)]
            # print(current, total, layover)
            ans = math.inf
            if layover >self.k+1:
                ans = math.inf
            elif current == self.dst:
                ans = 0
            else:
                # which ever
                if current in adj:
                    for info in adj[current]:
                        next_stop,cost = info
                        ans=min(ans,cost + helper(next_stop,layover+1))
            # print(best_cost)
            memo[(current, layover)] = ans
            return ans
        ans = helper(src,0)
        return -1 if ans == math.inf else ans