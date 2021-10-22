import math
class Solution:
    def minNonZeroProduct1(self, p: int) -> int:
        def getBinStr(n):
            b = bin(n)[2:]
            b = (p - len(b)) * '0' + b
            return b

        #zero = [0] * p
        #one = [0] * p
        #for i in range(1, 2**p):
        #    b = getBinStr(i)
        #    for j in range(0, p):
        #        if (b[j] == '0'):
        #            zero[j] += 1
        #        else:
        #            one[j] += 1
        zero = [2**(p-1) - 1] * p
        one = [2**(p-1)] * p
        print(zero, one)
        ret = 1
        for i in range(1, 2**p):
            b = getBinStr(i)
            v = 2**p
            for j in range(0, p):
                if (b[j] == '0'):
                    v = min(zero[j], v)
                else :
                    v = min(one[j], v)
            for j in range(0, p):
                if (b[j] == '0'):
                    zero[j] -= v
                else :
                    one[j] -= v
            ret = ret * i**v
        return ret % (1000000007)

    def minNonZeroProduct2(self, p: int) -> int:
        N = 2**p 

        ret = (N-2)**(N//2-1) * (N-1)

        return ret % (1000000007)

    def minNonZeroProduct3(self, p: int) -> int:
        N = 2**p 
        ret = 1
        n = (N-2) % (1000000007)
        print(N//2-1)
        for i in range(0, N//2-1):
            ret = (ret * n) % (1000000007)
        ret = ret * (N-1)
        return ret % (1000000007)

    def minNonZeroProduct4(self, p: int) -> int:
        N = 2**p 
        ret = 1
        n = (N-2) % (1000000007)
        if(p > 1):
            loop_cnt = int(math.log(N//2-1, 2) // 1)
            print(N//2-1, loop_cnt)
            loop_cnt2 = N//2-1
            if (loop_cnt):
                ret = n
                loop_cnt2 -= 2**loop_cnt
                for i in range(0, loop_cnt):
                    ret = ret * ret
                    ret = ret % (1000000007)
            for i in range(0, loop_cnt2):
                ret = (ret * n) % (1000000007)
                i = i * 2
        ret = ret * (N-1)
        return ret % (1000000007)

    def minNonZeroProduct(self, p: int) -> int:
        def expf(x, n):
            x = x % (1000000007)
            if (n == 0):
                return 1
            elif (n == 1):
                return x
            elif (n % 2):
                return x * expf(x * x, (n - 1)//2)
            else:
                return expf(x * x, n//2)

        N = 2**p 
        ret = expf(N-2, N//2-1)
        ret = ret * (N-1)
        return ret % (1000000007)

s = Solution()
print(s.minNonZeroProduct(60))