class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        minArr = [0] * len(nums)
        maxArr = [0] * len(nums)
        M = 0
        m = 1000000

        for i in range(len(nums)):
            maxArr[i] = M = max(nums[i], M)
            minArr[-i-1] = m = min(nums[-i-1], m)
        for i in range(len(nums)):
            if (maxArr[i] < minArr[i+1]):
                return i+1
        return None

s = Solution()
print(s.partitionDisjoint([5, 0, 3, 8, 6]))
