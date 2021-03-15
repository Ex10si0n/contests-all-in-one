'''
Algoritms: DFS
Efficiency: Better than normal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, path, result):
        if not root.left and not root.right: # if leaves
            result.append(path)
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val), result)
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val), result)

    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        self.dfs(root, str(root.val), result)
        return result

