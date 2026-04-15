# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(node, depth):
            if not node:
                return 0

            # if len(res) == depth:
            #     res.append([])

            res[depth].append(node.val)
            dfs(node.left, 1+depth)
            dfs(node.right, 1+depth)

        dfs(root, 0)
        return list(res.values())
