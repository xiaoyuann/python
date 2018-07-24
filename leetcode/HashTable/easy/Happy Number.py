class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dicts={}
        while n!=1:
            if n in dicts:
                return False
            else:
                dicts[n]=1
            n=sum([pow(int(c),2) for c in str(n)])
        return True