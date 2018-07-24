class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        l,maxs=1,1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                l+=1
                maxs=max(maxs,l)
            else:
                l=1
        return maxs
