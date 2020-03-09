"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''Solution
for max min in list:
    [..min..max..] -> max - min
    [..max...min..] : 
        [ ..max| ... | min... ]
           A      B     C
        only part A, B, C include answer
        B part can apply this function again
'''

class Solution:
    def maxProfit(self, prices):
        """find max profit in a list of stock price
        """
        # [max->min] -> 0
        temp = sorted(prices)[::-1]
        if temp == prices:
            return 0

        # simple situation
        prices_set = set(prices)
        max_index = prices.index(max(prices_set))
        min_index = prices.index(min(prices_set))
        print("Max Position: ",max_index,"\nMin Position: ",min_index)
        if max_index >= min_index :
            return prices[max_index]-prices[min_index]
        
        # 2th sitution 
        if max_index == 0:
            answer_A = 0
        else:
            answer_A = prices[max_index] - min(prices[:max_index])
        
        print("Part B: ",prices[max_index+1:min_index])
        if max_index == min_index - 1:
            answer_B = 0
        else:
            answer_B = self.maxProfit(prices[max_index+1:min_index])
        
        if min_index == len(prices)-1:
            answer_C = 0
        else:
            answer_C = max(prices[min_index+1:]) - prices[min_index]
        
        return max(answer_A,answer_B,answer_C)


if __name__ == "__main__":
    s = Solution()
    price1 = [7,1,5,3,6,4]
    price2 = [7,6,4,3,1]
    price3 = [11,4,7,2,1]
    print(s.maxProfit(price3))