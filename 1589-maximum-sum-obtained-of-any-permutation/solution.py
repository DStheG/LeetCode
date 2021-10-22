import operator
import heapq
class Solution:
    def maxSumRangeQuery0(self, nums: list[int], requests: list[list[int]]) -> int:
        d = {}
        for r in requests:
            for i in range(r[0], r[1]+1):
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        sorted_x = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        nums.sort(reverse=True)
        ret = 0
        for i, d in enumerate(sorted_x): 
            ret += (nums[i] * d[1])
        return ret % (10**9 + 7)

    def maxSumRangeQuery1(self, nums: list[int], requests: list[list[int]]) -> int:
        hist = [0] * 100000
        for r in requests:
            for i in range(r[0], r[1]+1):
                hist[i] += 1
        hist = list(filter(lambda x: x > 0, hist))

        nums.sort(reverse=True)
        hist.sort(reverse=True)

        ret = 0
        for i, h in enumerate(hist):
            ret += nums[i] * h
        return ret % (10**9 + 7)
    
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        hist = [0] * (len(nums) + 1) 
        for x, y in requests:
            hist[x] += 1
            hist[y+1] -= 1
        for i in range(1, len(hist)):
            hist[i] += hist[i-1]
        hist = list(filter(lambda x: x > 0, hist))

        nums.sort(reverse=True)
        hist.sort(reverse=True)

        ret = 0
        for i, h in enumerate(hist):
            ret += nums[i] * h
        return ret % (10**9 + 7)


s = Solution()
print(s.maxSumRangeQuery([1,2,3,4,5,10], [[0,2],[1,3],[1,1]]))