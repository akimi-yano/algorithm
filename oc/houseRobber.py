

houses = [1,2,3,8,5,9,8]
houses1 = [1,2,4,1,5,12,5]


def robbersHouse(houses):
  bag = []
  one_over = 0
  last = 0
  
  for robber in houses:
    if robber + one_over > last:
      bag.append(robber+one_over)
      one_over = bag[len(bag)-2]
      last =bag[len(bag)-1]
  print(bag)  
  return max(bag)
    
print(robbersHouse(houses))
print(robbersHouse(houses1))

  












