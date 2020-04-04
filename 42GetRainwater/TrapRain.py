"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

class Solution:
    def trap(self, height) -> int:
        '''
        '''
        trap = 0
        i = 0
        left = 0
        right = 0
        for i in range(1,len(height)-1):
            left = max(height[0:i])
            right = max(height[i+1:])
            if height[i]>=min(left,right):
                continue
            trap += (min(left,right)-height[i])
        return trap

if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))