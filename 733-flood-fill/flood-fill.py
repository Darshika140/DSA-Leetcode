class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original_color=image[sr][sc]
        if original_color==color:
            return image

        def dfs(sr,sc):
            m=len(image)
            n=len(image[0])

            if sr<0 or sc<0 or sr>=m or sc>=n:
                return
            
            if image[sr][sc]!=original_color:
                return

            image[sr][sc]=color
            
            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)

        dfs(sr,sc)

        return image
        