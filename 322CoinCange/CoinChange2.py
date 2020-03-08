"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 用备忘录解决了重叠子问题
# 是一种剪枝

class Solution:
    def coinChange(self,coins, amount: int):
        # 备忘录
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]

            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in set(coins):
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            
            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        
        return dp(amount)



if __name__ == "__main__":
    s = Solution()
    coins = [186,419,83,408]
    amount = 6249
    # coins = [1,3,5]
    # amount = 11
    print(s.coinChange(coins,amount))