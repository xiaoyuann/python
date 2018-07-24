class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num1 in nums:
            num2 = target - num1
            index1 = nums.index(num1)
            start_index = index1 + 1
            if num2 in nums[start_index:]:
                index2 = nums[start_index:].index(num2)
                return index1,index2+start_index
        