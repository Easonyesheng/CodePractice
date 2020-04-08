"""

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
"""

from queue import Queue

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        '''bfs
        '''
        x = 0
        y = 0
        count = 1
        searched = set()
        q = Queue()
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        q.put((x,y))
        searched.add((x,y))

        while not q.empty():
            x, y = q.get()
            for i in range(4):
                x_next = x + dx[i]
                y_next = y + dy[i]
                if x_next >= 0 and x_next < m and y_next >= 0 and y_next < n:
                    if (x_next,y_next) not in searched:
                        searched.add((x_next,y_next))
                        if x_next%10 + x_next//10 + y_next%10 + y_next//10 <= k:
                            count+=1
                            q.put((x_next,y_next))
                        
        return count

if __name__ == "__main__":
    s = Solution()
    m = 3
    n = 1
    k = 0 
    print(s.movingCount(m,n,k))