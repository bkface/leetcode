# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    def __init__(self):
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        combs = [""]
        for d in digits:
            combs = [x+c for x in combs for c in self.mapping[d]]
        return combs
        
