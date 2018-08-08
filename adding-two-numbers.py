'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        op = []
        bal = 0
        for i, j in reversed(zip(l1, l2)):
            t1 = i+j+bal
            bal = t1 // 10
            temp = t1 % 10
            op.append(temp)
        return op
c = Solution()
print c.addTwoNumbers([2, 4, 3], [5, 6, 4])