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

# 从海洋搜陆地，找到距离所有陆地最小距离最大的海洋为最优。
# 从每个海洋开始广度优先
# python 无法通过时间复杂度， 尝试用memo加速，出现未知错误
'''
from queue import Queue

class Solution:
    def maxDistance(self, grid) -> int:
        if not grid : return -1
        oceans = []
        max_dis = 0
        
        w, h = len(grid[0]), len(grid)
        for i in range(w):
            for j in range(h):
                if grid[i][j] == 0:
                    oceans.append((i,j))
        if not oceans or len(oceans) == w*h: return -1 
        for ocean in oceans:
            # print(ocean)
            ocean_searched = set()
            q = Queue()
            q.put((ocean,0))
            flag = False
            while not flag:
                (oi, oj), dis = q.get()
                ocean_searched.add((oi,oj))
                for add in (-1,1):
                    if oi+add >= 0 and oi+add < w:
                        if grid[oi+add][oj] == 1:
                            max_dis = max(max_dis, dis+1)
                            flag = True
                            break
                        else:
                            if (oi+add,oj) not in ocean_searched:
                                q.put(((oi+add,oj),dis+1))
                    if oj+add >= 0 and oj+add < h:
                        if grid[oi][oj+add] == 1:
                            max_dis = max(max_dis, dis+1)
                            flag = True
                            break
                        else:
                            if (oi,oj+add) not in ocean_searched:
                                q.put(((oi,oj+add),dis+1))
            # print("max: ",max_dis)
        return max_dis
'''
from queue import Queue

class Solution:
    def maxDistance(self, grid) -> int:
        '''bfs strat from ocean
        '''
        if not grid : return -1
        oceans = []
        # max_dis = 0
        memo = dict()
        # get oceans
        w, h = len(grid[0]), len(grid)
        for i in range(w):
            for j in range(h):
                if grid[i][j] == 0:
                    oceans.append((i,j))
        if not oceans or len(oceans) == w*h: return -1 

        # from ocean to search land use bfs
        for ocean in oceans:   
            # print('Start from:',ocean)
            q = Queue()
            q.put((ocean,0))
            flag = False
            while not flag:
                (oi, oj), dis = q.get()
                memo[(oi,oj)] = -1
                dis_memo =set()
                for add in (-1,1):
                    
                    if oi+add >= 0 and oi+add < w:
                        # print((oi+add,oj))
                        if grid[oi+add][oj] == 1:
                            # max_dis = max(max_dis, dis+1)
                            ocean_dis = dis+1
                            flag = True
                            break
                        else:
                            if (oi+add,oj) not in memo:
                                q.put(((oi+add,oj),dis+1))
                            elif memo[(oi+add,oj)] != -1:
                                # print('searched: ',(oi+add,oj),'is',memo[(oi+add,oj)])
                                dis_memo.add(memo[(oi+add,oj)]+dis)

                    if oj+add >= 0 and oj+add < h:
                        # print((oi,oj+add))
                        if grid[oi][oj+add] == 1:
                            # max_dis = max(max_dis, dis+1)
                            ocean_dis = dis+1
                            flag = True
                            break
                        else:
                            if (oi,oj+add) not in memo:
                                q.put(((oi,oj+add),dis+1))
                            elif memo[(oi,oj+add)] != -1:
                                # print('searched: ',(oi,oj+add),'is',memo[(oi,oj+add)])
                                dis_memo.add(memo[(oi,oj+add)]+dis)
                
                # print("Same dis search end")
                # print(dis_memo)
                if not flag and len(dis_memo) > 0: 
                    if min(dis_memo) < dis+2:                
                        dis = min(dis_memo)
                        ocean_dis = dis+1
                        # max_dis = max(max_dis,dis+1)
                        flag = True
                        break
                
            memo.update({ocean:ocean_dis})
            # print('memo: ',memo)
            # print(memo[(0,1)])

            # print("max: ",max_dis)
        return max(memo.values())


if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,0],[0,0,0],[0,0,0]]
    # grid = [[1,0,0,0,0,1,0,0,0,1],
    #         [1,1,0,1,1,1,0,1,1,0],
    #         [0,1,1,0,1,0,0,1,0,0],
    #         [1,0,1,0,1,0,0,0,0,0],
    #         [0,1,0,0,0,1,1,0,1,1],
    #         [0,0,1,0,0,1,0,1,0,1],
    #         [0,0,0,1,1,1,1,0,0,1],
    #         [0,1,0,0,1,0,0,1,0,0],
    #         [0,0,0,0,0,1,1,1,0,0],
    #         [1,1,0,1,1,1,1,1,0,0]]
    print(s.maxDistance(grid))