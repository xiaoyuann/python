class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        h = lambda s: list(map({}.setdefault,s,range(len(s))))
        return h(pattern)==h(str.split())