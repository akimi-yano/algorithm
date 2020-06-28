# Reconstruct Itinerary
# 「始点が "JFK" である有向準オイラーグラフが与えられるので、辞書順最小のオイラー路を出力せよ」

from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  
        adj_list = {}

        for ticket in tickets:
            if ticket[0] not in adj_list:
                adj_list[ticket[0]]=[ticket[1]]
            else:
                adj_list[ticket[0]].append(ticket[1])
        for key in adj_list.keys():
            adj_list[key].sort()
            adj_list[key] = deque(adj_list[key])
        # print(adj_list)
    
        def helper(cur_airport, num_tickets):
            if num_tickets < 1:
                return [cur_airport]
            if cur_airport not in adj_list:
                return None

            num_next = len(adj_list[cur_airport])
            for _ in range(num_next):
                next_airport = adj_list[cur_airport].popleft()
                next_itinerary = helper(next_airport, num_tickets-1)
                adj_list[cur_airport].append(next_airport)
    
                if next_itinerary is not None:
                    return [cur_airport] + next_itinerary
            return None
                

        return helper("JFK", len(tickets))