# https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in sorted(nums):
            ans += [i + [n] for i in ans]
        return ans
        
