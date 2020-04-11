"""
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 我们可以考虑使用动态规划来做这道题，状态可以表示成 (K, N)(K,N)，其中 KK 为鸡蛋数，NN 为楼层数。当我们从第 XX 楼扔鸡蛋的时候：

# 如果鸡蛋不碎，那么状态变成 (K, N-X)(K,N−X)，即我们鸡蛋的数目不变，但答案只可能在上方的 N-XN−X 层楼了。也就是说，我们把原问题缩小成了一个规模为 (K, N-X)(K,N−X) 的子问题；

# 如果鸡蛋碎了，那么状态变成 (K-1, X-1)(K−1,X−1)，即我们少了一个鸡蛋，但我们知道答案只可能在第 XX 楼下方的 X-1X−1 层楼中了。也就是说，我们把原问题缩小成了一个规模为 (K-1, X-1)(K−1,X−1) 的子问题。

# 这样一来，我们定义 dp(K, N)dp(K,N) 为在状态 (K, N)(K,N) 下最少需要的步数。根据以上分析我们可以列出状态转移方程：

# dp(K,N)=1+min(max(dp(K−1,X−1),dp(K,N−X)))  1<X<N

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。