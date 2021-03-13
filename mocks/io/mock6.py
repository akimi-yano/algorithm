"""
 I am running a school with portable units. I want to optimize the number of portable units based on the classes registered by students.
 
 Ex: At the beginning of the year I would publish the class schedule
 Math -> 9am-10am, 11am-12pm, 3pm-4pm
 Science-> 10am-11am, 3pm-4pm
 English -> 3pm - 4pm
 
 Then students register for classes. 
 John -> Math 9am-10am, Science 3pm-4pm
 Mark -> Science 10am-11am
 Levis -> English 3pm-4pm
 
 My goal is to figure out how many portable units I need to get to organize my school.
"""
'''
portable units = mobile class = room = 1 class at given time
optimizing = minimize the number of rooms

        r1   r2
9 -10am  M
10 -11am Science
3 - 4pm  Science  English

data needed:
subject and time (start, end)

3pm = 15

subject, start, end

process to make sure there is no duplicate  => remove duplicate
set([(time, subject)]) => list
cast it list
sort by start time 
duration is 1 hr each (assumption)
input: [(9, "M"), (9, "F"), (10,"Science"), (15,"Science"),(15,"English")]
                                                                       *
         cur_hour= 15 
         cur_subject = "English"
         cur_rooms = 2
         
         max_rooms = 2  

output: number of rooms 

input: [(9), (9), (10), (15),(15)]


'''
# after removing duplicate and sorted list
def get_rooms(arr):
    max_rooms = 0  
    cur_hour = None
    cur_subject = None
    cur_rooms = 0
    for time,  subject in arr:
        if time != cur_hour:
            cur_hour = time
            cur_subject = subject
            cur_rooms = 1
        else:
            cur_subject = subject
            cur_rooms += 1
            
        max_rooms = max(max_rooms, cur_rooms)
    
    return max_rooms
            

# print(get_rooms([(9, "Math"), (9, "French"), (10,"Science"), (15,"Science"),(15,"English"), (15, "French")]))
      
      
      
      
# improvement - no sorting
def room_num(arr):
    memo = {}
    for time, subject in arr:
        if time not in memo:
            memo[time] = set()
        memo[time].add(subject)
    
    return len(max(memo.values(), key = lambda x : len(x)))
    

print(room_num([(9, "Math"), (9, "French"), (10,"Science"), (15,"Science"),(15,"English"), (15, "French")]))