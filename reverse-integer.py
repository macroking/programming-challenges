'''
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        while(x != 0):
            t = x % 10
            x = x//10
            rev = rev * 10 + t
        return rev


s = Solution()
print s.reverse(120)
