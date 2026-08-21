# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Idea: initialize a new root which assign revert node
        TC:
        SC:
        """
        if root is None:
            return root
        tmp_root = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp_root)
        return root
    