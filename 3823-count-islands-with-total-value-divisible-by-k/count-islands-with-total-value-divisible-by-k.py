class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0

        def dfs(i,j):
            if (i<0 or j<0 or i>=m or j>=n or grid[i][j]==0):
                return 0

            total = grid[i][j]
            grid[i][j]=0 

            #Down
            total+=dfs(i+1,j)
            #up
            total+=dfs(i-1,j)
            #right
            total+=dfs(i,j+1)
            #left
            total+=dfs(i,j-1)

            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    total=dfs(i,j)

                    if total % k==0:
                        count+=1
        return count
        