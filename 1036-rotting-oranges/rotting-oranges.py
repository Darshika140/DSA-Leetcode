from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh=fresh+1
                    
        directions = [
            (0,1), #right
            (0,-1),#left
            (1,0), #down
            (-1,0) #up
        ]

        minutes=0

        #BFS
        while q and fresh>0:

            for _ in range(len(q)):
                current_row, current_col=q.popleft()

                for row_change, col_change in directions:
                    neigh_row=current_row+row_change
                    neigh_col=current_col+col_change

                    #checking boundaries 
                    if(0<=neigh_row<rows and 0<=neigh_col<cols and grid[neigh_row][neigh_col]==1):
                        grid[neigh_row][neigh_col]=2
                        fresh-=1

                        q.append((neigh_row, neigh_col))
            minutes+=1

        if fresh>0:
            return -1

        return minutes



        