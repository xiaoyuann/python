def moveZeroes():
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums=[0,1,4,0,5,0]
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums

print(moveZeroes())