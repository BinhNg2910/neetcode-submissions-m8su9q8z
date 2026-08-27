# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalancedCheck = True
        def dfsCheckBalance(root):
            nonlocal isBalancedCheck
            if root is None:
                return 0
            leftHeight = dfsCheckBalance(root.left)
            rightHeight = dfsCheckBalance(root.right)
            if abs(leftHeight - rightHeight) > 1:
                isBalancedCheck = False
            return 1 + max(leftHeight, rightHeight)
        dfsCheckBalance(root)
        return isBalancedCheck
        
            