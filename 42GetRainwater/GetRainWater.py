"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

#################################################
接完雨水，很容易看出这个数组有什么特点，就像一个山峰一样。
在最大值左边不严格递增，右边不严格递减。
因此只需要把原数组变成符合这样要求的数组就行了，改变的量就是接的雨水。

具体实现只需要先找到最大值索引，左右各自遍历一遍
两边都维护一个值来表示之前的最大值以保证单调性，
如果比最大值小，雨水量就加上这个差值，
如果大于等于，就更新最大值。

作者：duan-she-chi-8
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/zhao-gui-lu-tou-guo-xian-xiang-kan-ben-zhi-by-duan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def trap(self, height: list) -> int:
        if not height : return 0
        peek = height.index(max(height))
        left_max = 0
        right_max = 0
        trap = 0
        for i in range(peek):
            if height[i] < left_max:
                trap += (left_max-height[i])
            else:
                left_max = height[i]
            
        for j in range(len(height)-1,peek,-1):
            if height[j] < right_max:
                trap += (right_max-height[j])
            else:
                right_max = height[j]
        
        return trap

if __name__ == "__main__":
    s = Solution()
    height = []
    print(s.trap(height))