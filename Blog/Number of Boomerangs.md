# Number of Boomerangs
## [欢迎关注本人博客：云端筑梦师](http://www.cnblogs.com/Aurora-Twinkle/)

**题目:**

>Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

题意为假定平面上n个点两两都不同，boomerang解释为具有这样性质的由点组成的元组(i,j,k)：i到j的距离等于i到k的距离，顺序不同元组就不同。请找出n个点中所有的boomerang，返回总数，n最多为500，且坐标范围在[-10000,10000]之间。

**例如:**

``` python
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
```

**算法:**

``` python
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
```
算法思路是这样的，每次取一个点，算出这个点与剩下的所有点距离，并用一个哈希表存起来，例如，若有三个点到这个点的距离相同，则此距离的键值为3，根据排列组合的知识，这三个点可与取的点组成3*2个boomerang，以此类推，直到将points遍历完，对所有的boomerang求和即可。点击这里看[**原题**](https://leetcode.com/problems/number-of-boomerangs/description/)