"""
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

 

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 找n个数的公约数

class Solution:
    def hasGroupsSizeX(self, deck:list) -> bool:
        '''
        '''
        def cd(X,Y):
            '''find common divisor
            '''
            c_d = []
            for i in range(2,X+1):
                if X%i==0 and Y%i == 0:
                    c_d.append(i)
            return c_d

        
        cards = set(deck)
        if len(cards) < 1: return False
        
        nums = []
        for card in cards:
            nums.append(deck.count(card))
        nums.sort()
        print(nums)
        if len(nums) == 1: return nums[0]>=2
        X = nums[0]
        Y = nums[1]
        if X < 2: return False
        common_divisor = cd(X,Y)
        # print(common_divisor)
        if not common_divisor: return False
        for i in range(2,len(nums)):
            for j in common_divisor:
                if nums[i] % j == 0:
                    break
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    deck = [1,1]
    print(s.hasGroupsSizeX(deck))