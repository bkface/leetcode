# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, n in enumerate(nums):
            if target-n in d:
                return [d[target-n], i]
            d[n] = i
        
