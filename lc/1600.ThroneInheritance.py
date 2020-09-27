# 1600. Throne Inheritance
# Medium

# 11

# 46

# Add to List

# Share
# A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.

# The kingdom has a well-defined order of inheritance that consists of the king as the first member. Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.

# Successor(x, curOrder):
#     if x has no children or all of x's children are in curOrder:
#         if x is the king return null
#         else return Successor(x's parent, curOrder)
#     else return x's oldest child who's not in curOrder
# For example, assume we have a kingdom that consists of the king, his children Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.

# In the beginning, curOrder will be ["king"].
# Calling Successor(king, curOrder) will return Alice, so we append to curOrder to get ["king", "Alice"].
# Calling Successor(Alice, curOrder) will return Jack, so we append to curOrder to get ["king", "Alice", "Jack"].
# Calling Successor(Jack, curOrder) will return Bob, so we append to curOrder to get ["king", "Alice", "Jack", "Bob"].
# Calling Successor(Bob, curOrder) will return null. Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
# Using the above function, we can always obtain a unique order of inheritance.

# Implement the ThroneInheritance class:

# ThroneInheritance(string kingName) Initializes an object of the ThroneInheritance class. The name of the king is given as part of the constructor.
# void birth(string parentName, string childName) Indicates that parentName gave birth to childName.
# void death(string name) Indicates the death of name. The death of the person doesn't affect the Successor function nor the current inheritance order. You can treat it as just marking the person as dead.
# string[] getInheritanceOrder() Returns a list representing the current order of inheritance excluding dead people.
 

# Example 1:

# Input
# ["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
# [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
# Output
# [null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

# Explanation
# ThroneInheritance t= new ThroneInheritance("king"); // order: king
# t.birth("king", "andy"); // order: king > andy
# t.birth("king", "bob"); // order: king > andy > bob
# t.birth("king", "catherine"); // order: king > andy > bob > catherine
# t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
# t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
# t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
# t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
# t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
# t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]
 

# Constraints:

# 1 <= kingName.length, parentName.length, childName.length, name.length <= 15
# kingName, parentName, childName, and name consist of lowercase English letters only.
# All arguments childName and kingName are distinct.
# All name arguments of death will be passed to either the constructor or as childName to birth first.
# For each call to birth(parentName, childName), it is guaranteed that parentName is alive.
# At most 105 calls will be made to birth and death.
# At most 10 calls will be made to getInheritanceOrder.



# This solution does not work 

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
        
# class ThroneInheritance:

#     def __init__(self, kingName: str):
#         self.memo = {}
#         self.head = Node(None)
#         self.tail = Node(None)
#         new_node = Node(kingName)
#         self.head.next = self.tail.prev = new_node
#         self.head.next.next = self.tail
#         self.tail.prev.prev = self.head
#         self.memo[kingName] = new_node
        
#     def birth(self, parentName: str, childName: str) -> None:
#         if parentName in self.memo:
#             temp_node = self.memo[parentName].next 
#             new_node = Node(childName)
#             self.memo[parentName].next = new_node
#             new_node.next = temp_node
#             temp_node.prev = new_node
#             new_node.prev = self.memo[parentName]
#             self.memo[childName] = new_node

#     def death(self, name: str) -> None:
#         if name in self.memo:
#             node = self.memo[name]
#             node.prev.next, node.next.prev = node.next, node.prev
#             del self.memo[name]

#     def getInheritanceOrder(self) -> List[str]:
#         ans = []
#         cur = self.head.next
#         while cur.next:
#             ans.append(cur.val)
#             cur = cur.next
#         return ans


# # Your ThroneInheritance object will be instantiated and called as such:
# # obj = ThroneInheritance(kingName)
# # obj.birth(parentName,childName)
# # obj.death(name)
# # param_3 = obj.getInheritanceOrder()



# This solution does not work :

# class ThroneInheritance:

#     def __init__(self, kingName: str):
#         self.dead = set([])
#         self.adj_list = {}
#         self.adj_list[kingName] = []
#         self.root = kingName
#         self.ans = []
#         self.seen = set([])
        
#     def birth(self, parentName: str, childName: str) -> None:
#         self.helper(self.root,parentName, childName)
        
#     def helper(self, cur, parentName, childName):
#         if not cur:
#             return
#         if cur == parentName:
#             if cur not in self.adj_list:
#                 self.adj_list[cur] = [childName]
#             else:
#                 self.adj_list[cur].append(childName)
        
#         if cur not in self.adj_list:
#             return
#         for next_node in self.adj_list[cur]:
#             self.helper(next_node,parentName, childName)
            
    
#     def death(self, name: str) -> None:
#         self.dead.add(name)

#     def getInheritanceOrder(self) -> List[str]:
#         print(self.adj_list)
#         self.helper2(self.root)
#         return self.ans
        
#     def helper2(self, cur):
#         if not cur:
#             return
        
#         if cur in self.seen:
#             return
        
        
#         if cur not in self.dead:
#             self.ans.append(cur)
            
#         if cur not in self.adj_list:
#             return 
#         self.seen.add(cur)
#         for next_node in self.adj_list:
#             self.helper2(next_node)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()


# THIS SOLUTION WORKS !!!!!!
'''
don't forget to rest self.ans and self.seen !!!
'''


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set([])
        self.adj_list = {}
        self.adj_list[kingName] = []
        self.root = kingName
        self.ans = []
        self.seen = set([])
        
    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.adj_list:
            self.adj_list[parentName] = []
        self.adj_list[parentName].append(childName)
    
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # don't forget to rest self.ans and self.seen !!!
        self.ans = []
        self.seen = set([])
        
        self.helper(self.root)
        return self.ans
        
    def helper(self, cur):
        if not cur:
            return
        
        if cur in self.seen:
            return 
        self.seen.add(cur)
        
        if cur not in self.dead:
            self.ans.append(cur)
            
        if cur not in self.adj_list:
            return
        for next_node in self.adj_list[cur]:
            self.helper(next_node)



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()