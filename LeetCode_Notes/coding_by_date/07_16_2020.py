'''
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)*(len(nums)+1)/2
        for i in nums:
            total = total - i
        return int(total)


'''
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, root1, root2) -> bool:
        if (root1 == None and root2 == None):
            return True
        if (root1 != None and root2 != None):
            if (root1.val == root2.val):
                return (Solution().isMirror(root1.left, root2.right) and Solution().isMirror(root1.right, root2.left))
        return False
    def isSymmetric(self, root: TreeNode) -> bool:
        return Solution().isMirror(root, root)


'''
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: TreeNode) -> int:
        if (root == None):
            return 0
        return (max(Solution().height(root.left), Solution().height(root.right))) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if (root == None):
            return True

        leftHeight = Solution().height(root.left)
        rightHeight = Solution().height(root.right)

        if (abs(leftHeight - rightHeight) <= 1 and Solution().isBalanced(root.left) == True and Solution().isBalanced(
                root.right) == True):
            return True
        return False