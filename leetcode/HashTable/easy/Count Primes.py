class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        arr=[1]*n
        arr[:2]=[0,0]
        for i in range(2,int(n**0.5)+1):
            if arr[i]==1:
                arr[i*i::i]=[0]*len(arr[i*i::i])
        return sum(arr)
