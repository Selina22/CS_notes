'''
455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed factor gi,
which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
and the child i will be content. Your goal is to maximize the number of your content children
and output the maximum number.
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if (len(g) == 0 or len(s) == 0):
            return 0
        g.sort()
        s.sort()
        count = 0
        while (len(g) != 0 and len(s) != 0):
            if (s[0] >= g[0]):
                count += 1
                s.remove(s[0])
                g.remove(g[0])
            else:
                s.remove(s[0])
        return count


'''
435. Non-overlapping Intervals
Given a collection of intervals, find the minimum number of intervals you need to remove 
to make the rest of the intervals non-overlapping.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if (len(intervals) == 0):
            return 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        count = 0
        endpoint = intervals[0][1]
        for i in range(1, len(intervals)):
            if (intervals[i][0]<endpoint):
                count+=1
            else:
                endpoint = intervals[i][1]
        return count


'''
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list1 = headA
        list2 = headB
        iterA = headA
        iterB = headB
        while (iterB!=iterA):
            if (list1 != None):
                list1 = list1.next
            else:
                iterB = iterB.next
            if (list2 != None):
                list2 = list2.next
            else:
                iterA = iterA.next
        return iterA
