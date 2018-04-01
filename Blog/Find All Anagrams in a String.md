# Find All Anagrams in a String
## [欢迎关注本人博客：云端筑梦师](http://www.cnblogs.com/Aurora-Twinkle/)

**题目:**
>Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

题意为给定一个字符串s和一个非空字符串p，找出s中所有是p的anagrams的子串的起始索引,所有字符串均由小写字母组成，且字符串长度不超过20100，将结果以列表形式返回，不必考虑列表的顺序。感兴趣的童鞋可以戳这里看[**原题**](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/)

**例如:**
``` python
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

**算法:**

先上代码，这里用python3实现：
``` python
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
```
思路是这样的，考虑到字符串由小写字母组成，所以可利用哈希表和ascii编码，字母的编码范围是65~122，所以可以创建连个长度为123键值全为0的哈希表，先对p遍历，将p中出现的字母及次数用哈希表phash记录下来，再依次遍历s的每个字母并记录到shash，并与phash进行比对，若相等，则说明找到了一个anagrams，将此时的起始索引存进res列表即可，直到s遍历完，返回res。

