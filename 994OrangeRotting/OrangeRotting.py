"""
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from queue import Queue

class Solution:
    def orangesRotting(self, grid) -> int:
        '''Use BFS
            put orange location in a set - target
            put rot_location and time in a quene
            use BFS
            until target is empty, return time

        '''

        # get grid size
        w = len(grid[0])
        h = len(grid)

        # get the target & rot
        target = set()
        rot = set()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    target.add(str(i)+str(j))
                if grid[i][j] == 2:
                    rot.add(str(i)+str(j))
        if len(target) == 0:
            return 0
        # print(rot)
        q = Queue()
        for i in range(len(rot)):
            q.put((rot.pop(),0))
            # print('q',q.get())
        while not q.empty():
            rot_loc, time = q.get()
            # print('get out: ',rot_loc)
            for i in range(2):
                for add in (-1,1):
                    # print(rot_loc)
                    if (int(rot_loc[i])+add) < 0 or (i==0 and (int(rot_loc[i])+add)==h) or (i==1 and (int(rot_loc[i])+add)==w):
                        continue
                    cur = rot_loc[:i]+str(int(rot_loc[i])+add)+rot_loc[i+1:]
                    # print(cur,i,add)
                    if cur in target:
                        # print("put in: ",cur)
                        q.put((cur,time+1))
                        target.remove(cur)
                        if len(target) == 0:
                            return time+1
                        
        return -1


if __name__ == "__main__":
    s = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(s.orangesRotting(grid))
