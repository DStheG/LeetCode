class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        idx = 0
        p = 0
        while(idx < len(bits)):
            if(bits[idx] == 0):
                p = 0
                idx+=1
            else:
                p = 1
                idx+=2
        return not p and idx == len(bits)


s = Solution()
print(s.isOneBitCharacter([0, 0]))