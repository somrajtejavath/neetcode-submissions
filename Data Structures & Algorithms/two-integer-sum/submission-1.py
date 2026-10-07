class Solution:
    def twoSum(self,nums,target):
        vis = {}

        for i in range(len(nums)):
            curr = nums[i]

            if target-curr in vis:
                return[vis[target-curr],i]
            else:
                vis[curr] = i
