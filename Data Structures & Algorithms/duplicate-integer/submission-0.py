class Solution:
    def hasDuplicate(self, nums):
        vis = set()
        for i in range(len(nums)):
            curr = nums[i]

            if curr in vis:
                return True

            vis.add(curr)
        return False