class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        cnt = 0
        for n in nums:
            if (n == 1):
                cnt += 1
                if (cnt > m):
                    m = cnt
            else:
                if (cnt > m):
                    m = cnt
                cnt = 0
        return m