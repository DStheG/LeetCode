class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''.join([str(c) if c.isdigit() else ' ' for c in word])
        return len(set([int(n) for n in s.split()]))

s = Solution()
print(s.numDifferentIntegers("a1b01c001"))