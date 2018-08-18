# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        MCMXCIV
        """
        d1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        d2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        ans = 0
        indices = range(len(s))
        for i in indices:
            if s[i] in ["I", "X", "C"]:
                if i < len(s) - 1 and s[i:i+2] in d2:
                    ans += d2[s[i:i+2]]
                    indices.remove(i+1)
                    continue
            ans += d1[s[i]]
        return ans
        
