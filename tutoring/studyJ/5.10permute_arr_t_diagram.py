'''
perm = [2,0,1,3]
A = ['a','b','c','d']

A[perm[i]],A[i] => swap
perm[perm[i]],perm[i] => swap
until perm[i]==i

        0 1 2 3 
perm = [2,0,1,3]
A = ['a','b','c','d']
----
i=0
1. perm[i]==i ? No
i=0
perm[i]=2

2. 
A[perm[i]] = A[2]
A[i] = 'a'

A = ['c','b','a','d']

3. 
perm[perm[i]] = perm[2]=1
perm[i] = 2 

perm = [1,0,2,3]
----
i=1
1. perm[i]=i ?  No
i=1
perm[i]=0

2. 
A[perm[i]]=A[0]='c'
A[i]='b'

A = ['b','c','a','d']

3.
perm[perm[i]] = perm[0]=1
perm[i] = 0

perm = [0,1,2,3]

----
i=2
1. perm[i]=2? Yes
'''