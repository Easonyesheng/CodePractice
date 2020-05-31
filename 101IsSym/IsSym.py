"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。



"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrror(root.left, root.right)

    def isMirrror(self, left, right):
        if (not left) and (not right):
            return True
        elif not (left and right):
            return False
        else:
            return left.val == right.val and self.isMirrror(left.left,right.right) and self.isMirrror(left.right,right.left)

