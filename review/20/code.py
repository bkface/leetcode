# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        d = {"(": ")", "[": "]", "{": "}"}
        stack = ""
        for i in s:
            if i in d.keys():
                stack += i
                continue
            if len(stack) == 0:
                return False
            else:
                if d[stack[-1]] != i:
                    return False
                stack = stack[:-1]
        if len(stack) == 0:
            return True
        else:
            return False
        
