'''
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        if (len(numbers) == 0):
            return None
        while (head < tail):
            two_sum = numbers[head] + numbers[tail]
            if (two_sum == target):
                return [head + 1, tail + 1]
            elif (two_sum < target):
                head += 1
            elif (two_sum > target):
                tail -= 1
        return None


'''
653. Two Sum IV - Input is a BST
Given a Binary Search Tree and a target number, return true if there exist two elements 
in the BST such that their sum is equal to the given target.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: TreeNode, vals, target):
        if root == None:
            return
        Solution().inOrder(root.left, vals, target)
        vals.append(root.val)
        Solution().inOrder(root.right, vals, target)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        vals = []
        Solution().inOrder(root, vals, k)
        vals.sort()
        head = 0
        tail = len(vals) - 1
        while (head < tail):
            twoSum = vals[head] + vals[tail]
            if (twoSum == k):
                return True
            if (twoSum < k):
                head += 1
            else:
                tail -= 1
        return False


‘’‘
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
’‘’
#can try quick sort algo for this later
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
   
