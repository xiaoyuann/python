class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==0:
            return False
        length=len(bits)
        turn=0
        while turn<length:
            if turn==length-1:
                return True
            if bits[turn]==1:
                turn+=2
            else:
                turn+=1
        return False
