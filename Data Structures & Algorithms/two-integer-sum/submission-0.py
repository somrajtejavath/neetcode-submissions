class Solution:
    def twoSum(self,nums,target):

        vis = {}

        for i in range(len(nums)):
            curr = nums[i]
            comp = target -curr

            if comp in vis:
                return [vis[comp],i]
            else:
                vis[curr] = i
            
