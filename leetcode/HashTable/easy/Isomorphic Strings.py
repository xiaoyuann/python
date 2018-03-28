class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1,d2={},{}
        for i,val in enumerate(s):
            d1[val]=d1.get(val,[])+[i]
        for j,val1 in enumerate(t):
            d2[val1]=d2.get(val1,[])+[j]
        return sorted(d1.values())==sorted(d2.values())