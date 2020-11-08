'''
Ki Master Youseikouza

A: 3-1 Union Find - basic x
B: 3-2 Union Find - optimization x
C: 4-1 Segment Tree - concept x
D: 4-2 Segment Tree - one point update range output x
E: 4-3 Segment Tree - range update one point output x
F: 4-4 Segment Tree - recursive approach x
G: 7-1 Splay Tree
H: 7-2 Splay Tree
I: 7-3 Splay Tree
J: 8-1 Link-Cut Tree
K: 8-2 Link-Cut Tree
'''

# << UNION FIND >>　　

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


# << SEGMENT TREE >>

# C: 4-1 Segment Tree
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


# D: 4-2 Segment Tree
'''
adding the value at the index and return the sum of the range
'''

class SEG_TREE:
    def __init__(self, nums):
        self.SEG_LEN = 1  << 18
        self.seg = [0 for _ in range(self.SEG_LEN * 2)]

        for i, value in enumerate(nums):
            self.add(i, value)
            # print(self.seg, i, value)
            
    # one point 
    def add(self, idx, val):
        idx += self.SEG_LEN
        self.seg[idx] +=  val
        while True:
            idx //= 2
            if idx == 0: 
                break
            self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]
            
    # range 
    def sum(self, l,r):
        r += 1
        l += self.SEG_LEN
        r += self.SEG_LEN
        ans = 0
        while l < r:
            if l %  2  == 1:
                print(l)
                ans += self.seg[l]
                l+=1
            l//=2
            if r %  2  == 1:
                ans += self.seg[r-1]
                r-=1
            r//=2
        return  ans  

seg_tree = SEG_TREE([1, 3, 5])
# Given nums = [1, 3, 5]

print(seg_tree.sum(0, 2))
# sumRange(0, 2) -> 9

seg_tree.add(1,-3)
seg_tree.add(1,2)
# update(1, 2)

print(seg_tree.sum(0, 2))
# Given nums = [1, 2, 5]
# sumRange(0, 2) -> 8



# E: 4-3 Segment Tree

'''
adding the value to all the values within the range and return the value of a point
'''

class SEG_TREE2:
    def __init__(self, nums):
        self.SEG_LEN = 1  << 18
        self.seg = [0 for _ in range(self.SEG_LEN * 2)]

        for i, value in enumerate(nums):
            self.add(i, i, value)
            # print(self.seg, i, value)
            
    # one point 
    def get(self, idx):
        idx += self.SEG_LEN
        sum = 0
        sum += self.seg[idx] 
        while True:
            idx //= 2
            if idx == 0: 
                break
            sum += self.seg[idx] 
        return sum 
            
    # range 
    def add(self, l, r, val):
        r += 1
        l += self.SEG_LEN
        r += self.SEG_LEN
        ans = 0
        while l < r:
            if l %  2  == 1:
                self.seg[l] += val
                l+=1
            l//=2
            if r %  2  == 1:
                self.seg[r-1] += val 
                r-=1
            r//=2
        
seg_tree2 = SEG_TREE2([1, 3, 5])
# Given nums = [1, 3, 5]

print(seg_tree2.get(0))
print(seg_tree2.get(1))
print(seg_tree2.get(2))

seg_tree2.add(0,2,-5)

print(seg_tree2.get(0))
print(seg_tree2.get(1))
print(seg_tree2.get(2))



# F: 4-4 Segment Tree
'''
recursive approach
set val (one point) and get min (range)
'''

class SEG_TREE3:
    def __init__(self, nums):
        self.SEG_LEN = 1  << 3
        self.seg = [0 for _ in range(self.SEG_LEN * 2)]

        for i, value in enumerate(nums):
            print(i, value)
            self.set_val(i, value)
            # print(self.seg, i, value)
            
    # one point 
    def set_val(self, pos, val):
        pos += 1 << 2
        self.seg[pos] = val
        while True:
            pos//=2
            if pos < 1:
                break
            self.seg[pos] = min(self.seg[pos*2], self.seg[pos*2+1])
            
    # range 
    def get_min(self, ql, qr, sl = 0 , sr = 1 << 2, pos =  1):
        # chittomo kabutte nai 
        if  qr <= sl or sr <= ql:
            return float('inf')
        # kannzennni tsutsumareteru 
        if ql <= sl and sr <= qr:
            return self.seg[pos]
        sm = (sl + sr) //2 
        lmin = self.get_min(ql, qr, sl, sm, pos * 2)
        rmin = self.get_min(ql, qr, sm, sr, pos * 2 + 1)
        return min(lmin, rmin)


seg_tree3 = SEG_TREE3([1, 3, 5])
# Given nums = [1, 3, 5]
print(seg_tree3.seg)
print(seg_tree3.get_min(0,2+1))
print(seg_tree3.set_val(1,-1))
print(seg_tree3.seg)
print(seg_tree3.get_min(0,2+1))
print(seg_tree3.set_val(2,-2))
print(seg_tree3.seg)
print(seg_tree3.get_min(0,2+1))
print(seg_tree3.get_min(1,1+1))

