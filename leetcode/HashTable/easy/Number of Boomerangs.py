from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points):
        num=0
        for x1,y1 in points:
            distance=defaultdict(int)
            for x2,y2 in points:
                dx=x1-x2
                dy=y1-y2
                d=dx**2+dy**2
                distance[d]+=1
            num+=sum(n*(n-1) for n in distance.values())
        return num