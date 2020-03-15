"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 不要呀字符串！
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        '''
        dfs
        '''
        # wide and height
        w, h = len(grid[0]), len(grid)
        print(w,h)
        max_area = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    temp_stack = []
                    temp_area = 0
                    temp_stack.append((i,j))
                    grid[i][j] = 0
                    while len(temp_stack) > 0:
                        i,j = temp_stack.pop()
                        print(i,',',j)
                        temp_area += 1
                        
                        if i>0:#up
                            if grid[i-1][j] == 1:
                                temp_stack.append((i-1,j))
                                grid[i-1][j] = 0
                        if i < h-1:#down
                            if grid[i+1][j] == 1:
                                temp_stack.append((i+1,j))
                                grid[i+1][j] = 0
                        if j > 0:#left
                            if grid[i][j-1] == 1:
                                temp_stack.append((i,j-1))
                                grid[i][j-1] = 0
                        if j < w-1:#right
                            if grid[i][j+1] == 1:
                                temp_stack.append((i,j+1))
                                grid[i][j+1] = 0
                    print('(',i,j,')',temp_area)
                    max_area = max(max_area,temp_area)
        return max_area

if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0],
            [1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0],
            [0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0],
            [1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1],
            [0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1]]
    print(s.maxAreaOfIsland(grid))


                            


