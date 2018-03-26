class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxk=sum(nums[:k])
        temp=maxk
        for i in range(len(nums)-k):
            temp=temp-nums[i]+nums[i+k]
            if temp>maxk:
                maxk=temp
        return maxk / k