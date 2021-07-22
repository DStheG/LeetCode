class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        def getMandn(pivot):    
            return max(nums[:pivot]), min(nums[pivot:])
        pivot = 1
        M, m = getMandn(pivot)
        while (M > m):
            print (M, m)
            pivot= pivot + nums[pivot:].index(m) + 1
            M, m = getMandn(pivot)
        return pivot
        
s = Solution()
print(s.partitionDisjoint([1,1,1,0,6,12]))
