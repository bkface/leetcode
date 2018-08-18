# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        lastPos = 1
        curN = nums[0]
        for i in xrange(1, len(nums)):
            if (nums[i] != curN):
                nums[lastPos] = nums[i]
                curN = nums[i]
                lastPos += 1
        return lastPos

