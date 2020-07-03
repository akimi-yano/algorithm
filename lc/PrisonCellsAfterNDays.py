# Prison Cells After N Days

# There are 8 prison cells in a row, and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, 
# then the cell becomes occupied.
# Otherwise, it becomes vacant.

# (Note that because the prison is a row, the first and the last cells in the row can't 
# have two adjacent neighbors.)

# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell 
# is occupied, else cells[i] == 0.

# Given the initial state of the prison, return the state of the prison after N days (and N such 
# changes described above.)


# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:

# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]


# Note:

# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9



# this  doesnt  work
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # print(cells)
        for _ in  range(N):
            temp = [] 
            for i in range(len(cells)):
                if i == 0 or i == len(cells)-1:
                    temp.append(0)
                else:
                    a =cells[i-1]^cells[i+1]
                    a = a&0
                    temp.append(a)
            cells = temp
            # print(cells)
        return cells
    


# this  works

# Solution 1
# We record all seen states.
# Be careful,
# we need transform array to string as the key,
# otherwise it use the reference.


# Python:

    def prisonAfterNDays(self, cells, N):
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells

# this  works

# Solution 2
# I tried to find the pattern of the loop.
# Well, the length of loop can be 1, 7, or 14.

# So once we enter the loop, every 14 steps must be the same state.

# The length of cells is even,
# so for any state, we can find a previous state.
# So all states are in a loop.

# It means that, after a single step from the initial state, we enter the loop.


# Python: 
# whenN=0  as it is. 
# when N=1 is the same as when N=15 (never go back to the starting state as 
# everything becomes [0] at the start and end)

    def prisonAfterNDays(self, cells, N):
        N -= max(N - 1, 0) // 14 * 14
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells
    
    
# finally got to  this  conclusion and it  works!!!

class Solution:
        # there is a pattern of the loop: the length of loop can be 1, 7, or 14.
        # So once we enter the loop, every 14 steps must be the same state.
        # The length of cells is even, so for any state, we can find a previous state.
        # So all states are in a loop.
        # It means that, after a single step from the initial state, we enter the loop.
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # if N == 0: #N  is always larger than or equal to 1 according to the rule
        #     return cells
        if N > 14:
            N = N%14
        if N%14 == 0:
            N = 14
        # print(cells)
        # print(N)
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            # print(cells)
        return cells
    
    


# Further  worked on this and this is the solution I like the most

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # print(cells)
        cells = [0]+[cells[i-1]^cells[i+1]^1 for i in range(1,7)]+[0]
        N -= 1
        
        num_changed = 0
        patterns = []
        patterns_dict = {}
        while N > 0:
            cells_str = ''.join([str(cell) for cell in cells])
            if cells_str in patterns_dict:
                break
            patterns.append(cells_str)
            patterns_dict[cells_str] = num_changed
            cells = [0]+[cells[i-1]^cells[i+1]^1 for i in range(1,7)]+[0]
            N -= 1
            num_changed += 1

        # if N went to 0 before we found a repeat
        if N < 1:
            return cells
        
        # print(patterns_dict)
        cycle_size = num_changed - patterns_dict[cells_str]
        N = N % cycle_size
        return_str = patterns[N]
        return_cells = [int(cell_str) for cell_str in return_str]
        return return_cells