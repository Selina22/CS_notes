'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 2):
            return n
        prev1 = 1
        prev2 = 2
        for i in range(2, n):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr


'''
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        curr = 0
        for i in range(0, len(nums)):
            curr = max(prev1, nums[i]+prev2)
            prev2 = prev1
            prev1 = curr
        return curr
            

'''
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses 
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def rob_by_pos(self, nums: List[int], start: int, end: int):
        prev1 = 0
        prev2 = 0
        curr = 0
        for i in range(start, end):
            curr = max(prev1, nums[i]+prev2)
            prev2 = prev1
            prev1 = curr
        return curr
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        if (total == 1):
            return nums[0]
        return max(Solution().rob_by_pos(nums, 0, total-1), Solution().rob_by_pos(nums, 1, total))
        

'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Java HashMap
'''
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numTable = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numTable.containsKey(target - nums[i])) {
                return new int[]{numTable.get(target - nums[i]), i};
            } 
            else {
                numTable.put(nums[i], i);
            }
        }
        return null;
    }
}
