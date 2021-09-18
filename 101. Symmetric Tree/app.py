from typing import Optional
from data_structures import BinaryTreeNode as TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirrorRecursive(self, left, right):
        if left == None and right == None:
            return True
        elif left != None and right != None:
            return (
                left.val == right.val
                and self.isMirror(left.left, right.right)
                and self.isMirror(left.right, left.right)
            )

    def isMirrorIterative(self, left, right):
        pass
