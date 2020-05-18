# 1453. Maximum Number of Darts Inside of a Circular Dartboard
# User Accepted:457
# User Tried:1410
# Total Accepted:499
# Total Submissions:2934
# Difficulty:Hard
# You have a very large square wall and a circular dartboard placed on the wall. 
# You have been challenged to throw darts into the board blindfolded. 
# Darts thrown at the wall are represented as an array of points on a 2D plane. 
# Return the maximum number of points that are within or lie on any circular dartboard of radius r.


def numPoints(self, p: List[List[int]], r: int) -> int:
    eps = 1e-8
    def dist(p1,p2):
        return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1])**2)**0.5
    def getCircleCenter(p1,p2):
        mid = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
        angle = math.atan2(p1[0]-p2[0],p2[1]-p1[1])
        d = (r*r-pow(dist(p1,mid),2))**0.5
        return (mid[0]+d*math.cos(angle),mid[1]+d*math.sin(angle))

    N = len(p)
    ans = 1
    for i in range(N):
        for j in range(i+1, N):
            if dist(p[i],p[j]) > 2*r : continue
            center = getCircleCenter(p[i],p[j])
            cnt = 0
            for k in range(N):
                if dist(center,p[k]) < 1.0*r+eps: cnt+=1
            ans = max(ans,cnt)
    return ans
