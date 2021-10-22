class Solution:
    def reverseBits(self, n: int) -> int:
        b = "{0:032b}".format(n)
        rn = b[::-1]
        return int(rn, 2)