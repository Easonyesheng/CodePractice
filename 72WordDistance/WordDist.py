"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# bottom to top

class Solution:
    def minDistance(self, word1, word2):
        '''
        '''

        l1, l2 = len(word1), len(word2)

        if l1*l2 == 0:
            return l1+l2
        
        Dp = [[0]*(l2+1) for _ in range(l1+1)]

        for i in range(l1+1):
            Dp[i][0] = i
        
        for i in range(l2+1):
            Dp[0][i] = i

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                add_2 = Dp[i-1][j] + 1
                cut_2 = Dp[i][j-1] + 1
                relate = Dp[i-1][j-1] 
                if word2[j-1] != word1[i-1]:
                    relate += 1
                Dp[i][j] = min(add_2, cut_2, relate)

        return Dp[l1][l2]

if __name__ == "__main__":
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    print(s.minDistance(word1, word2))