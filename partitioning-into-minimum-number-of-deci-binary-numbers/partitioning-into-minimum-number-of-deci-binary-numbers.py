class Solution:
    def minPartitions(self, n: str) -> int:
        l = [int(i) for i in n]
        s = set(l)
        return max(s)