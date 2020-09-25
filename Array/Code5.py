#5.买卖股票的最佳时机
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        min_p=prices[0]#设定一个最小值
        max_p=0#设定一个最大值记录最佳时机获得的利润
        for i in range(len(prices)):
            min_p= min(min_p,prices[i])
            max_p= max(max_p,prices[i]-min_p)#最大利润=max{前一天最大利润, 今天的价格 - 之前最低价格}
        return max_p