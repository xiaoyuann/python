class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        numss=sorted(nums)
        if numss[-1]>=2*numss[-2]:
            return nums.index(numss[-1])
        return -1