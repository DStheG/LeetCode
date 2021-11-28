class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        ret = []
        @functools.cache
        def MUL(i):
            if (i >= len(nums)):
                return 1
            return MUL(i+1) * nums[i]
        for i in range(len(nums)):
            ret.append(acc * MUL(i+1))
            acc = acc * nums[i]
            
        return ret