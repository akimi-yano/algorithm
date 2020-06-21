# 5441. Making File Names Unique
        # 1st - without
        # 2nd - (1)
        # 3rd = (2)
        # if - (1) in memo:
        #     add (1) (2) to kaido 
        #     add it twice if the name includes (1)
        
# this does not work
# class Solution:
#     def getFolderNames(self, names: List[str]) -> List[str]:
#         memo = {}
#         ans = []
#         for name in names:
#             if name not in memo:
#                 memo[name]=1
#                 ans.append(name)
#                 if name[len(name)-1]==")":
#                     for i in range(len(name)):
#                         if name[i] == "(":
#                             original = name[:i]
#                             num=""
#                             i+=1
#                             while name[i]!=")":
#                                 num+=name[i]
#                                 i+=1
#                             if original in memo:
#                                 memo[original]=int(num)+1
#             else:
#                 memo[name]+=1
#                 new_name = name+"("+str(memo[name]-1)+")"
#                 number = memo[name]-1
#                 while new_name in memo:
#                     new_name = new_name+"("+str(number)+")"  
#                     number+=1
#                 # print(new_name)
#                 ans.append(new_name)
#                 memo[new_name] = 1
#                 if new_name[len(new_name)-1]==")":
#                     for i in range(len(new_name)):
#                         if new_name[i] == "(":
#                             original = new_name[:i]
#                             num=""
#                             i+=1
#                             while new_name[i]!=")":
#                                 num+=new_name[i]
#                                 i+=1
#                             if original in memo:
#                                 memo[original]=int(num)+1

#         return ans
                

# This works   
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = {}
        ans = []
        for name in names:
            if name not in memo:
                memo[name]=1
                ans.append(name)
            else:
                new_name = name+"("+str(memo[name])+")"
                memo[name]+=1
                while new_name in memo:
                    new_name = name+"("+str(memo[name])+")"  
                    memo[name]+=1
                ans.append(new_name)
                memo[new_name] = 1

        return ans
                