'''
https://codeinterview.io/playback/POYYURIJTT#?t=1609

implement color fill / paint fill

input:
x, y - where - integers
canvas - what - 2D
color -what with - Color object {}

fill()


output:
no output - modify in place


name: fill()
input 
output




/ O 
- fill background 
- fill within the shape

'''


def traverse(row, col, canvas, color, prev_color):
    # check of the row and col are valid
    if not (0 <= row < len(canvas)) or not (0 <= col < len(canvas[0])):
        return
    # IMPORTANT: if the color of the current spot is not the same as the prev_color: return
    if canvas[row][col] != prev_color:
        return
    canvas[row][col] = color
    traverse(row, col+1, canvas, color, prev_color)
    traverse(row, col-1, canvas, color, prev_color)
    traverse(row-1, col, canvas, color, prev_color)
    traverse(row+1, col, canvas, color, prev_color)
    
def fill(row, col, canvas, color):
    prev_color = canvas[row][col]
    # Edge Case: if the color is same color as the prev_color, it could go stack overflow 
    # and we dont need to color the place with the same color
    if color != prev_color:
        traverse(row, col, canvas, color, prev_color)
        
    
    
    