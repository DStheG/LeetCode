import functools
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        divisible = [0 for i in range(0, 1000)]
        nums.sort()
        @functools.cache
        def dfs(idx):
            if (idx == len(nums)):
                return 0
            n = nums[idx]
            ret = 1
            for i in range(idx+1, len(nums)):
                if (nums[i] % n == 0):
                    ret = max(dfs(i) + 1, ret)
            return ret
        l = 0
        for i in range(0, len(nums)):
            l = max(dfs(i), l)
        v = 1
        ret = []
        for i in range(0, len(nums)):
            if (dfs(i) == l and nums[i] % v == 0):
                ret.append(nums[i])
                v = nums[i]
                l -= 1
                if (l == 0):
                    break
        return ret
        
s = Solution()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4,8]))
print(s.largestDivisibleSubset([1,2,3,4,6,24]))