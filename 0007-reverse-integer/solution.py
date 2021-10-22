class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if (x < 0) :
            neg = True
            x = -x
        X = str(x)[::-1]
        ret = int(X) * (-1 if neg else 1)
        if (ret > 2**31 - 1):
            return 0
        if (ret < -2**31):
            return 0
        return ret
