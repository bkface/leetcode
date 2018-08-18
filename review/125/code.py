# https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2: return True
        ps = 0
        pe = len(s)-1
        while(ps < pe):
            if not s[ps].isalpha() and not s[ps].isdigit():
                ps += 1
                continue
            if not s[pe].isalpha() and not s[pe].isdigit():
                pe -= 1
                continue
            if s[ps].lower() != s[pe].lower():
                return False
            ps += 1
            pe -= 1
        return True
        
