# 729. My Calendar I
# Medium

# 2584

# 69

# Add to List

# Share
# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.


# This solution works:


from sortedcontainers import SortedList
class MyCalendar:
    '''
    We need to make sure that q1 == q2, that is that the point we we need to insert start and end is in the same gap.
    Also q1 % 2 == 0, because it should be gap between two intervals, see [1, 3), [5, 10). If we found that we need to insert both start and end to [3, 5), it is OK for us, if to [1, 3) or [5, 10) it is not OK.
    Complexity
    Time complexity of one book is O(log n), time complexity of all algorithm is O(n log n). Space complexity is O(n).
    '''
    def __init__(self):
        self.s_list = SortedList()

    def book(self, start: int, end: int) -> bool:
        left = self.s_list.bisect_right(start)
        right = self.s_list.bisect_left(end)
        if left == right and left % 2 == 0:
            #can insert
            self.s_list.add(start)
            self.s_list.add(end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)