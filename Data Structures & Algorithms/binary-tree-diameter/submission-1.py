# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Idea: make a recursion function to return max length of just one path from root to its leaf, get max on left and right then compare which the global max diamter
        TC: O(n)
        SC: O(h) -> O(n) -> h = n
        n is number of node
        """
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            if node is None:
                return 0
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            maxDiameter = max(maxDiameter, maxLeft + maxRight)
            return 1 + max(maxLeft, maxRight)

        maxDiameter = 0
        _ = dfs(root)
        return maxDiameter
        