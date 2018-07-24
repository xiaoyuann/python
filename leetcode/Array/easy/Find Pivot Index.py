class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=sum(nums)
        lsum=0
        for i in range(len(nums)):
            sums-=nums[i]
            if lsum==sums:
                return i
            lsum+=nums[i]
        return -1