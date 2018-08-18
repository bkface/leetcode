# https://leetcode.com/problems/word-break/description/

class Solution(object):
    def __init__(self):
        self.not_matched = set()

    def wordBreak(self, s, wordDict, idx=0):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if idx == len(s):
            return True
        
        if idx in self.not_matched:
            return False

        for w in wordDict:
            if s[idx:idx+len(w)] == w and self.wordBreak(s, wordDict, idx+len(w)):
                return True
        self.not_matched.add(idx)
        return False
        
