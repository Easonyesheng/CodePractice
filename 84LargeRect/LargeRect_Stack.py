"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入: [2,1,5,6,2,3]
输出: 10
"""
# 单调栈 两边决定中间值，用单调栈
# 每次pop出来的，是可以确定的，其左边小值就是栈中前一个，右边小值则是正在入栈的一个。

class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                area = max(area, h * (i - stack[-1] - 1))
            stack.append(i)
        heights.pop()
        return area


