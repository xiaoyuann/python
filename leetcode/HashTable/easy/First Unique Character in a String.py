class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l)==1]
        return min(index) if len(index)>0 else -1
        '''
        a=[]
        for item in set(s):
            if s.count(item)==1:
                a.append(s.index(item))
        if len(a)>0:
            return min(a)
        else:
            return -1
        '''