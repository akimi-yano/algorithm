# 8.1 implement a stack with max API

# Design a stack that includes a max operation, in addition to push and pop. 
# The max method should return the maximum value stored in the stack.

class Stack:
    def __init__(self):
        self.storage = []
        self.max_vals = []
        
    def push_to_bottom(self,val):
        if len(self.max_vals)==0 or self.max_vals[len(self.max_vals)-1]<=val:
            self.max_vals.append(val)
        self.storage.append(val)
        return self
    def pop_bottom(self):
        if len(self.storage)==0:
            return 
        popped = self.storage.pop()
        if self.max_vals[len(self.max_vals)-1] == popped:
            self.max_vals.pop()
        return popped
    
    def get_max(self):
        print("MAX VALUE")
        return self.max_vals[len(self.max_vals)-1]
    
    def print_vals(self):
        print("STACK VALUES")
        for num in self.storage:
            print(num)
        

new_stack = Stack()
new_stack.push_to_bottom(1).push_to_bottom(2).push_to_bottom(3).push_to_bottom(4).push_to_bottom(5).push_to_bottom(5).push_to_bottom(4)
print(new_stack.get_max())
new_stack.pop_bottom()
print(new_stack.get_max())
new_stack.pop_bottom()
print(new_stack.get_max())
new_stack.pop_bottom()
print(new_stack.get_max())
new_stack.print_vals()
new_stack.push_to_bottom(100)
print(new_stack.get_max())

    