class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=collections.Counter(nums)
        return max([count[x]+count[x+1] for x in count if count[x+1]],default=0)