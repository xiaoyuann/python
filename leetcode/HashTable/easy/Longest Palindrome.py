from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for item in s:
            if item not in hash:
                hash.add(item)
            elif item in hash:
                hash.remove(item)
        return len(s)-len(hash)+1 if len(hash)>0 else len(s)

class Solutions(object):
    def longestPalindrome(self, s):
        c = Counter(s)
        return sum(v - 1 * (v % 2 != 0) for v in c.values()) + 1 * any(v % 2 != 0 for v in c.values())