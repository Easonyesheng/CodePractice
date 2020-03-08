"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 动态规划
# 面对一些问题还是会超时

class Solution:
    def coinChange(self, coins, amount):
        '''Dynamic Programming
            F(coins,amount) = 1 + min(F(coins,amount-i) for i in coins)
            :para 
                coins : a list for coins we have
                amount : the value we need to get
            :output
                the minimum numbers of coins we need 
        '''
        if amount == 0: # ...
            return 0 
        # sort
        coins.sort()
        coins_rev = coins[::-1]
        
        # print(coins_rev)
        if amount < min(coins):
            return -1
        elif amount in coins:
            return 1
        else:
            for i in coins_rev:
                if i % amount == 0:
                    n = amount / i
                    return n
                    
                elif i < amount:
                    index = coins_rev.index(i)+1
                    if index == len(coins_rev):
                        return -1

                    times = amount // i
                    temp = self.coinChange(coins,amount-i*times)
                    while temp == -1:
                        times -= 1
                        temp = self.coinChange(coins_rev[index:],amount-i*times)
                        if times == 0:
                            times = 1
                        
                    return times + temp
                    
        return  -1



if __name__ == "__main__":
    s = Solution()
    # coins = [186,419,83,408]
    # amount = 6249
    coins = [1,3,5]
    amount = 110003
    print(s.coinChange(coins,amount))