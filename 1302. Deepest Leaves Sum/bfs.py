
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # maintain the BFS iteration state in the frontier queue 
        # Insert a None between every two levels in the queue
        frontier, leafSum = deque([root, None]), 0

        # Perform BFS
        while len(frontier) > 0:
            node = frontier.popleft()
            if node:
                leafSum += node.val
                for child in [node.left, node.right]:
                    # Don't add extra Nones to the frontier
                    if child:
                        frontier.append(child)
            elif len(frontier) > 0 and frontier[-1] is not None:
                # We found a deeper level, so zero out the leafSum variable
                leafSum = 0
                # Add a None to the front of the queue to mark the begining of the new level
                frontier.append(None)

        # Return result
        return leafSum
