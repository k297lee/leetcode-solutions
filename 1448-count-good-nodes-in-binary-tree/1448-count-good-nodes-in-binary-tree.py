# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                self.res += 1
            nextMax = max(node.val, currMax)
            traverse(node.left, nextMax)
            traverse(node.right, nextMax)
        
        traverse(root, -100001)
        return self.res