from functools import reduce
import operator
class Solution(object):
#version1
    def singleNumber21(self,nums):
        return 2*sum(set(nums))-sum(nums)

#version2

    def singleNumber22(self,nums):
        dict={}
        for num in nums:
            dict[num]=dict.get(num,0)+1
        for key,val in dict.items():
            if val==1:
                return key

#version3
    def singleNumber23(self,nums):
        res=0
        for num in nums:
            res ^= num
        return res

#version4
    def singleNumber24(self,nums):
        return reduce(lambda x,y:x^y,nums)

#version5
    def singleNumber25(self,nums):
        return reduce(operator.xor,nums)