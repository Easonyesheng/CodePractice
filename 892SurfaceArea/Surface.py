"""
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。

 

示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],[3,4]]
输出：34
示例 3：

输入：[[1,0],[0,2]]
输出：16
示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def surfaceArea(self, grid) -> int:
        '''
        for every grid has x cubes:
            (y cudes for border grid)
            S_x = 6x - (2x-2) - ∂(y==0)(y if y<x else x)

        '''
        if not grid : return 0

        w,h = len(grid[0]), len(grid)
        S = []
        for i in range(w):
            for j in range(h):
                # vertical
                if grid[i][j] == 0: continue
                S_temp = 4*grid[i][j] + 2
                for a in (1,-1):
                    if i+a >= 0 and i+a <w :
                        if grid[i+a][j] != 0:
                            area_loss = grid[i+a][j] if grid[i+a][j]<grid[i][j] else grid[i][j]
                            S_temp -= area_loss
                
                    if j+a >=0 and j+a < h:
                        if grid[i][j+a] != 0:
                            area_loss = grid[i][j+a] if grid[i][j+a]<grid[i][j] else grid[i][j]
                            S_temp -= area_loss
                S.append(S_temp)
        return sum(S)

if __name__ == "__main__":
    s = Solution()
    grid = [[1,2],[3,4]]
    print(s.surfaceArea(grid))