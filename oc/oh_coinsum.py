def coinsum(coins, total):
  cache = {}
  
  def find_ways(cur, start_from):
    result = 0
    key = cur, start_from
    if key in cache:
      return cache[key]
      
    if cur == 0:
      return 1
    if cur < 0:
      return 0
  
    for i in range(start_from, len(coins)):
      result += find_ways(cur-coins[i], i)
      
    cache[key] = result
    
    return result
    
  return find_ways(total, 0)
  
print(coinsum([2,5,3,6], 10))




