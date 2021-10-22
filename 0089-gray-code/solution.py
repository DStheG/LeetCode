class Solution:
    def grayCode(self, n: int) -> list[int]:
        if (n == 1):
            return [0, 1]
        l = self.grayCode(n-1)
        ret = []
        n = 2 ** (n-1)
        coeff = 0
        for e in l:
            ret.append(e + n * coeff)
            coeff = not coeff
            ret.append(e + n * coeff)
        return ret

s = Solution()
print(s.grayCode(2))