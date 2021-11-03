import functools
import heapq
class Solution:
    def canJump0(self, nums: list[int]) -> bool:
        @functools.lru_cache()
        def jump(idx):
            if (idx >= len(nums)):
                return False
            if (idx == len(nums)-1):
                return True
            n = nums[idx]
            for i in range(1, n+1):
                if (jump(idx+i)):
                    return True
            return False

        return jump(0)

    def canJump1(self, nums: list[int]) -> bool:
        rn = nums[::-1]
        n = 0
        h = []
        heapq.heappush(h, 0)
        while(len(h)):
            print(h)
            n = heapq.heappop(h)
            for j in range(n+1, len(rn)):
                if(n >= j - rn[j]):
                    if(j == len(rn)-1):
                        return True
                    heapq.heappush(h, j)
        return False

    def canJump(self, nums: list[int]) -> bool:
        if(len(nums) == 1):
            return True
        def jump(l, r):
            if(l >= len(nums)-1 or r >= len(nums)-1):
                return True
            M = 0
            for i in range(l, r+1):
                M = max(M, nums[i] + i)
            if(M < r+1):
                return False
            return jump(r+1, M)

        return jump(0, 0)

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([2,0]))
print(s.canJump([2,0,0]))