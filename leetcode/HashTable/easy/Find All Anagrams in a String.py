class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        m,n=len(s),len(p)
        phash=[0]*123
        shash=[0]*123
        if n>m:return res
        for i in p:
            phash[ord(i)]+=1
        for i in s[:n-1]:
            shash[ord(i)]+=1
        for i in range(n-1,m):
            shash[ord(s[i])]+=1
            if i-n>=0:
                shash[ord(s[i-n])]-=1
            if shash==phash:
                res.append(i-n+1)
        return res
