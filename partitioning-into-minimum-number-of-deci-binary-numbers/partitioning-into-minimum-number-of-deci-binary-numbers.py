class Solution:
    def minPartitions(self, n: str) -> int:
        m = -1
        for i in n:
            print(i)
            if int(i) > m:
                m = int(i)
            if m == 9:
                return m
        return m