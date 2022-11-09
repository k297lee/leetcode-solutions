# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root.left and not root.right:
                return int("".join([str(x) for x in curr + [root.val]]))
            
            total = 0
            if root.left:
                total += dfs(root.left, curr + [root.val])
            
            if root.right:
                total += dfs(root.right, curr + [root.val])
            
            return total
        
        return dfs(root, [])