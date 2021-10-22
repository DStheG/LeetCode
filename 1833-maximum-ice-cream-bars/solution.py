class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ret = 0
        for c in costs:
            coins -= c
            if (coins < 0):
                break
            ret += 1
        return ret