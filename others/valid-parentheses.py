'''
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

'''

def check( a, b):
    if a == '(' and b != ')' or \
        a == '{' and b != '}' or \
        a == '[' and b != ']':
        return False
    return True

def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for bracket in s:
        if bracket in '{[(':
            stack.append(bracket)
        else:
            if not stack or not check(stack.pop(), bracket):
                return False

    return False if stack else True

print isValid('{[)}]')