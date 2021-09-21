class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        def flip(nums, idx, k):
            for i in range(idx, idx+k+1):
                if (i >= len(nums)):
                    break
                if nums[i] == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0
            return nums
        ret = 0
        for i in range(len(nums)):
            print(nums)
            if(nums[i] == 0):
                ret += 1
                nums = flip(nums, i, k)
        return ret

s = Solution()
print(s.minKBitFlips([0,1,0], 1))