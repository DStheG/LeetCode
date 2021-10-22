class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        re_cust = []
        carry = 0
        for c in customers:
            if (c + carry) > 4 :
                v = 4
                carry = c + carry - 4
            else:
                v = c + carry
                carry = 0
            re_cust.append(v)
        while(carry > 0):
            re_cust.append(min(carry, 4))
            carry -= 4

        maxProfit = 0
        profit = 0
        ret = -1
        print(customers, sum(customers))
        print(re_cust, sum(re_cust))
        p = []
        for idx, c in enumerate(re_cust):
            profit += (c * boardingCost - runningCost)
            p.append(profit)
            if profit > maxProfit:
                maxProfit = profit
                ret = idx + 1
        print(p)
        return ret
        

s = Solution()
print(s.minOperationsMaxProfit([10,10,6,4,7], 3, 8))

