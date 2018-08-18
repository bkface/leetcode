# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        done = set()
        ans = set()
        for i, t in enumerate(nums):
            if t in done:
                continue
            done.add(t)
            d = set()
            for j in xrange(i+1, len(nums)):
                n = nums[j]
                s = 0-t-n
                if s in d:
                    ans.add(tuple(sorted([t, n, s])))
                d.add(n)
        return list(ans)
        
