# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                if idx != i:
                    nums[idx] = nums[i]
                    nums[i] = 0
                idx += 1
        
