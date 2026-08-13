# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        def dfs(node,col,row):
            if not node:
                return 
            nodes.append((col, row, node.val))
            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
        dfs(root,0,0)
        nodes.sort()

        ans=[]
        prev_col=None
        for col, row, val in nodes:
            if col!=prev_col:
                ans.append([])
                prev_col=col

            ans[-1].append(val)
            
        return ans 



        