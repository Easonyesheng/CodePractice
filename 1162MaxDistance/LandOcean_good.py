"""
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。

 

示例 1：



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：



输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 从陆地扩展，最后扩展到的海洋就是最优的
# 岛屿问题用标记
# 方向数组！ 
import collections

class Solution:
    def maxDistance(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        start = []
        for i in range(rows): # 将所有起点存入 start 数组
            for j in range(cols):
                if grid[i][j] == 1:
                    start.append((i, j, 0))
        
        if len(start) == 0 or len(start) == rows * cols: # 特判
            return -1

        queue = collections.deque(start) # 队列初始化
        dr = [0, 1, 0, -1] # 建立方向数组
        dc = [1, 0, -1, 0]
        while queue:
            i, j, dis = queue.popleft()
            for d in range(4): # 四个方向
                x = i + dr[d]
                y = j + dc[d]
                if x < 0 or y < 0 or x == rows or y == cols or grid[x][y] == 1: 
                    continue
                queue.append((x, y, dis + 1))
                grid[x][y] = 1 # 访问过的位置标记为 1
                
        return dis 

if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    print(s.maxDistance(grid))