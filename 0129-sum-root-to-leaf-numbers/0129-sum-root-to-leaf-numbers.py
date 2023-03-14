# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(cur=None, path=''):
            nonlocal ans
            if cur:
                path += str(cur.val)
                dfs(cur.left, path)
                dfs(cur.right, path)
                if cur.left == None and cur.right == None:
                    ans += int(path)
            return
        dfs(root)
        return ans