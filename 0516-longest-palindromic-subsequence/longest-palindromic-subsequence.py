class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def findP(l: int, r: int) -> int:
            if (l == r):
                return 1
            elif (l > r):
                return 0
            if (s[l] == s[r]):
                return findP(l+1, r-1) + 2
            else:
                return max(findP(l+1, r), findP(l, r-1))
        return findP(0, len(s)-1)
