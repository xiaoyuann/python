class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstRow=set("QWERTYUIOP")
        secondRow=set("ASDFGHJKL")
        thirdRow=set("ZXCVBNM")
        lists=[]
        for word in words:
            string=set(word.upper())
            if string<=firstRow or string<=secondRow or string<=thirdRow:
                lists.append(word)
        return lists