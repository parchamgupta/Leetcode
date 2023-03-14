# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        def dfs(cur=None, path=''):
            nonlocal ans
            if cur:
                path = chr(97 + int(cur.val)) + path
                dfs(cur.left, path)
                dfs(cur.right, path)
                if cur.left == None and cur.right == None:
                    if ans is None:
                        ans = path
                    else:
                        ans = min(ans, path)
            return
        dfs(root)
        return ans