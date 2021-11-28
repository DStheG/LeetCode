import functools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def travel(i, j):
            if(i == m and j == n):
                return 1
            if(i > m or j > n):
                return 0
            return travel(i+1, j) + travel(i, j+1)
        return travel(1, 1)

s = Solution()
print(s.uniquePaths(3, 2))
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 3))