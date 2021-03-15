'''
Algorithms Tags: DFS
Efficiency: Normal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if targetSum == root.val and not root.left and not root.right:
            return True
        l = r = False
        if root.left:
            l = self.hasPathSum(root.left, targetSum-root.val)
        if root.right:
            r = self.hasPathSum(root.right, targetSum-root.val)
        return l or r
