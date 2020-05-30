"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入: [2,1,5,6,2,3]
输出: 10
"""
# !O(n^2) TimeError
class Solution:
    def largestRectangleArea(self, heights) -> int:
        Area = 0
        for i in range(len(heights)):
            if i >=1 and heights[i] == heights[i-1]: continue
            temp = self.GetArea(heights,i)
            # print(temp)
            Area = max(Area, temp)
        
        return Area

    def GetArea(self, heights, index):
        '''Get the area of the index 
        '''
        height = heights[index]
        if height == 0: return 0
        width = 1
        # To left
        for i in range(index-1,-1,-1):
            if heights[i] >= heights[index]:
                width +=1
            else:
                break
        
        # To right
        for i in range(index+1,len(heights)):
            if heights[i] >= heights[index]:
                width +=1
            else:
                break
        
        return height*width


if __name__ == "__main__":
    S = Solution()
    heights = [2,1,5,6,2,3]
    print(S.largestRectangleArea(heights))