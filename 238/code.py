# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1 for n in nums]
        lp = 1
        rp = 1

        for i in xrange(len(nums)-1):
            lp *= nums[i]
            ans[i+1] *= lp

        for i in xrange(len(nums)-1, 0, -1):
            rp *= nums[i]
            ans[i-1] *= rp

        return ans
        
