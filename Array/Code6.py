#6.买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #算出每天股票之间的差价存入列表
        l1 = []
        for i in range(len(prices)):
            if i < len(prices)  - 1:
                k = i + 1
                l1.append(prices[k] - prices[i])
        #股票需要最获利就等于把每天获利的加起来
        ans = 0
        for i in l1:
            if i > 0:
                ans += i
        return ans

