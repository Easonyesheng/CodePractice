"""
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False
"""

# dfs with dictionary
# dfs -- stack
# bfs -- quene

# from queue import Queue

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        '''
        '''
        if z > x+y:
            return False
        if self.judge_situ(x,y,z):
            return True
        memo = set()
        # q = Queue()
        # q.put((x,y))
        stack = []
        stack.append((x,y))
        while stack:
            can1, can2 = stack.pop()
            memo.add((can1,can2))
            for i in range(6):
                can1_temp, can2_temp = self.can_change(can1,can2,x,y,i)
                if (can1_temp,can2_temp) in memo:
                    continue
                else:
                    if self.judge_situ(can1_temp,can2_temp,z):
                        return True
                    else:
                        stack.append((can1_temp,can2_temp))
        return False


    def can_change(self, can1, can2, can1_v, can2_v, situ):
        '''Can situation can function
        :para
            can1 : waters in can1
            can2 : waters in can2
            can1_v : volume of can1
            can2_v : volume of can2
            situ : how to change
                0: empty can1
                1: full can1
                2: can1 to can2
                3: empty can2
                4: full can2
                5: can2 to can1
        :output
            can1_c : changed can1 water
            can2_c : changed can2 water
        '''
        if situ == 0:
            can1_c = 0
            can2_c = can2

        elif situ == 1:
            can1_c = can1_v
            can2_c = can2

        elif situ == 2:
            if can1+can2 <= can2_v:
                can1_c = 0
                can2_c = can1+can2
            else:
                can1_c = can1 - (can2_v - can2)
                can2_c = can2_v
        
        elif situ == 3:
            can2_c = 0
            can1_c = can1
        
        elif situ == 4:
            can2_c = can2_v
            can1_c = can1
        
        elif situ == 5:
            if can1 + can2 <= can1_v:
                can1_c = can1+can2
                can2_c = 0
            else:
                can1_c = can1_v
                can2_c = can2 - (can1_v - can1)
    
        return can1_c, can2_c


    def judge_situ(self,can1,can2,z):
        '''Judge the situation is the wanted or not
        :para
            same as above
        :output 
            bool
        '''
        if can1 == z or can2 == z or (can1+can2) == z:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    x = 3
    y = 4
    z = 5
    print(s.canMeasureWater(x, y, z))