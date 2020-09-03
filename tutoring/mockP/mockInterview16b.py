'''        

x y
points = [(1,2),(2,1),(0,0)]

P = (3,3)

def distance(point1,point2):
    pass
    
  input 
  (distance function)
  points = [(x,y)...]
  P = (px,py)
    
  output k closest points to the P
  [(ox,oy)]
  
  - if there is tie -> does that matter ? 
  
  [() ...]
  n -> [(d, idx)]
  sort by d ( n log n)
  left -> k. k <- right (k)
  
- sort
- minheap
- maxheap

'''

'''

High level(design and details) -> Low level (pseudo code / coding)
# Making Collaborative TODO list (PM system)
Requirements (and Features) What is Collab TODO? (website + mobile):
  tasks with categories
  
    list shooping:
        task A
        task C
        task B
        
    list study for interview:
        task A
        task C
        task B
  
  Make task objects belonging to specific list groups
  # make task for a group list 
  
  make the task movable to drag and drop 
  -> you can move the task between different list 
  
  # * think of edge cases: 0 ? 1 ? many ? 
  if we cannot move:
    cons: 
      have to delete / and recreate (people might want to remove it) 
        api calls ? ui ux decisions
      might need a feature to retrieve the data (reliability, consistancy)
        extra code to handle data loss -- caching storage ...
       
    pros:
      prevent from accidental data loss
        maybe we dont need the caching / storage for data reliability
      potentially prevent from higher latency/ expensive operations
        less load on our servers maybe we dont need as many (Cost)
   
    elif we can move:
        cons:
            accidentally moved/deleted 
            expensive
            someone might hold onto card, what happens if there is disconnect between
                cache and backend?
        pros:
            visually pleasant
            easy to use
            intuitive -> other apps do this too! why cant we?
            
shopping = [{name:"A"},{name:"C"}]
study_list = [{name:"A"},{name:"B"},{name:"C"} ,{name:"B"},]
# moving shopping_B to end of study_list
def move_object(starting_list, destination_list, obj, curr_idx, next_idx):
    destination_list.insert(obj, next_idx)
    starting_list.pop(curr_idx)
    return

working with objects -> what do we know about the object?
    we know the list it belongs to,
    we know the contents it has,
    we know the current index/position
    we need to know next index/position (we also need the next list)

Technical challenges (depend on the decision, what are your workarounds? roadmap/planning):
    load balancer (for expensive / high load)
        how many requests?
        average statistics
        read vs write
    requests / second multiply result with _________
    data loss -> reliability -> db(sharding, replicas), cache
              -> server -> api -> more functions because more handling
                                -> more code, more tests, more Q&A
                                -> more time, more money, oh no ):
                                -> more maintenance more labor oh no ):
    cache -> write-through (offline mode, save the state and do db transaction when online at once) / write-around (related to data loss)
          -> ui / ux does the user need to have immediate feedback?
          -> long polling vs sockets (requests, vs number connections)
    list capacity (scalability issue) 
        -> change structure on backend (SLL, DLL, ...)
        -> change structure on frontend (truncate results / chunk results in cache)
        -> change structure on both (: (pagination and requested rendering)
    
DB:

API:


JavaScript
    angular / react cdk (drag and drop)
    jquery ui 


'''