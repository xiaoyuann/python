class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums1:
            if i in nums2 and i not in a:
                a.append(i)
        return a
        # return list(set(nums1)&set(nums2))