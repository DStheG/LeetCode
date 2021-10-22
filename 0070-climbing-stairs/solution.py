from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=45)
        def sol(n):
            if(n <= 2):
                return n
            return sol(n-2) + sol(n-1)
        return sol(n)

s = Solution()
print(s.climbStairs(3))