class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col=len(grid),len(grid[0])
        perimeter=0
        for y in range(row):
            for x in range(col):
                if grid[y][x]==1:
                    perimeter+=4
                    if x<col-1 and grid[y][x+1]==1:
                        perimeter-=2
                    if y<row-1 and grid[y+1][x]==1:
                        perimeter-=2
        return perimeter