'''
Ki Master Youseikouza

A: 3-1 Union Find - basic x
B: 3-2 Union Find - optimization x
C: 4-1 Segment Tree
D: 4-2 Segment Tree
E: 4-3 Segment Tree
F: 4-4 Segment Tree
G: 7-1 Splay Tree
H: 7-2 Splay Tree
I: 7-3 Splay Tree
J: 8-1 Link-Cut Tree
K: 8-2 Link-Cut Tree
'''

# UNION FIND　　

# A: 3-1 Union Find - basic
def union_find(n, edges):
    roots = [i for i in range(1,n+1)]
    # Optimization 2 (make sure that the tree is not deep)
    depths = [1 for _ in range(1,n+1)]
    def find(x):
        # you dont have parent ! -> return yourself
        if x == roots[x-1]:
            return x
        else:
            # B: 3-2 Union Find - optimization 
            # Optimization 1 (memorization by updating the roots in the array)
            roots[x-1] = find(roots[x-1])
            return roots[x-1]
        
    def union(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            # SAME PARENTS - CYCLE
            return 1
        # B: 3-2 Union Find - optimization x
        # Optimization 2 (make sure that the tree is not deep)
        # 浅い方の親を深い方の親にくっつける。
        if depths[x-1] > depths[y-1]:
            x,y = y,x 
        if depths[x-1] == depths[y-1]:
            depths[y-1]+=1
        roots[x-1]=y - 1
        # UNIONED
        return 0
    
    print("before calling union", roots)
    for fr,to in edges:
        union(fr,to)
    for k in range(1,n+1):
        find(k)
    print("after calling union and find ", roots)



edges = [(1,2),(1,4),(1,3),(2,4),(3,5),(4,5)]
union_find(5,edges)


            #    1
            #  /\  \ 
            # 3  4 - 2
            # \ /  
            #  5


# SEGMENT TREE 

# SEG 木　列を管理するデータ構造
# できる操作　
# １：区間の更新　（足し算、上書き）
# ２：区間の集約の取得　（和、最小値）

# 基本アイデア：
    #　完全二分木の葉に値を保存
    #　各頂点に子孫の集約を保存

    #           O
    #        /    \
    #      O       O
    #     /\       /\ 
    #   O   O    O   O 
    #  /\  /\   /\   /\
    # O O  O O O O  O O     <- the values are saved at the leaves !  
    
    # width  : N
    # height : logN

# update from bottom 
# the updating itself is O(1)

# [a~b) -> a以上b未満　*bは入らない
