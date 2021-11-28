import bisect
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        tbl = [[] for i in range(0, 100+1)]
        for i, t in enumerate(temperatures):
            tbl[t].append(i)

        ret = []
        acc = [[] for i in range(0, 100+1)]
        for i in range(99, 29, -1):
            acc[i] = acc[i+1] + tbl[i+1]
            acc[i].sort()

        for i, t in enumerate(temperatures):
            result = bisect.bisect_right(acc[t], i)
            if (len(acc[t]) == result):
                ret.append(0)
            else:
                ret.append(acc[t][result] - i)
        return ret

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([30,60,90]))