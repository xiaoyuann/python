class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict={u:i for i,u in enumerate(list1)}
        s,result=1e9,[]
        for j,v in enumerate(list2):
            i=dict.get(v,1e9)
            if i+j < s:
                s=i+j
                result=[v]
            elif i+j==s:
                result.append(v)
        return result
