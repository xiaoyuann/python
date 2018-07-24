from collections import Counter
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(Counter(t)-Counter(s))[0]
       #return chr(reduce(operator.xor,map(ord,s+t)))