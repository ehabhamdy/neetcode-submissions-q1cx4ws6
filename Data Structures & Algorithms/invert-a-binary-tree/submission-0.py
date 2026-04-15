# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        def backtrack(node: Optional[TreeNode]):
            if node == None:
                return

            tmp = node.left
            node.left = node.right
            node.right = tmp

            backtrack(node.left)
            backtrack(node.right)

        backtrack(root)

        return root

        