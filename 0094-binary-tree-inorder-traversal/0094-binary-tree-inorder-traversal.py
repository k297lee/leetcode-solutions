# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right:
                    tmp = tmp.right
                
                tmp.right = curr
                tmp2 = curr
                curr = curr.left
                tmp2.left = None
        
        return res