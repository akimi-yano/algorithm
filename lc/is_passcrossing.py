
def isPathCrossing(path):
    visited = set([(0,0)])
    s_row = 0
    s_col = 0
    memo = {'N':(1,0),'S':(-1,0),'E':(0,1),'W':(0,-1)}
    for p in path:
        if p in memo:
            row, col = memo[p]
            s_row+=row
            s_col+=col
            if (s_row,s_col) in visited:
                return True
            visited.add((s_row,s_col))
    return False
    
print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))

                
                
        