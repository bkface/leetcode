# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution(object):
    def bs(self, nums, target, left, right):
        while left <= right:
            pos = (left+right)/2
            n = nums[pos]
            if target == n:
                return pos
            elif target < n:
                right = pos-1
            else:
                left = pos+1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)-1
        if nums[left] <= nums[right]:
            return self.bs(nums, target, left, right)

        max_pos = -1
        while left <= right:
            pos = (left+right)/2
            n = nums[pos]
            if n > nums[left]:
                left = pos
            else:
                right = pos
            if left == right:
                max_pos = pos
                break

        max_n = nums[max_pos]
        min_n = nums[max_pos+1]
        if target > max_n or target < min_n:
            return -1
        elif min_n <= target <= nums[len(nums)-1]:
            return self.bs(nums, target, max_pos+1, len(nums)-1)
        else:
            return self.bs(nums, target, 0, max_pos)

