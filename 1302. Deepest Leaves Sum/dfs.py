# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumLeaves: int = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.sumNodeAtDepth(root, getDepth(root))
        return self.sumLeaves

    def sumNodeAtDepth(self, root, targetDepth, currDepth=0):
        """
        Perform DFS
        add root value to self.sumLeaves when we find the deepest level
        """
        if root is None:
            return

        if targetDepth == currDepth:
            self.sumLeaves += root.val

        self.sumNodeAtDepth(root.left, targetDepth, currDepth+1)
        self.sumNodeAtDepth(root.right, targetDepth, currDepth+1)

def getDepth(root, d=0):
    """
    Peform DFS
    return the max depth at each level
    """
    if root is None:
        # We have gone too far since root is None, hence the -1
        return d-1

    # Compare the max depth on the left and right side.
    # Return the depth of the deepest subtree
    return max(getDepth(root.left, d+1), getDepth(root.right, d+1))
