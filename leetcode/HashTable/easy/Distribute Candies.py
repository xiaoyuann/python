class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return len(candies)//2 if len(candies)//2<len(set(candies)) else len(set(candies))