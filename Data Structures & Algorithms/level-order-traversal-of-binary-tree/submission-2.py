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

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return [None, 0]

            # if len(res) == depth:
            #     res.append([])
            
            res[depth].append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 0)

        return list(res.values())