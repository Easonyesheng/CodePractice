"""LeetCode 752
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：

 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 

每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
"""
# 将 0000 到 9999 看作10000种状态，以每个状态为节点构成一个图
# 根节点为 0000 ，每个节点之间相距1，意为转动一次到达
# 所以需要找到从root到target的最短路径
# 因为广度优先搜索（BFS）偏向于找到离根近的节点，所以用BFS

from queue import Queue

class Solution:
    def openLock(self, deadends, target) :
        '''main part for solution
            :para
                deadends : the list that we cannot be same
                target : the right number we need to get
            :output
                step : how many rotation we need to open the lock 
        '''

        #python in 针对 list 平均复杂度O(n), 对于 set 和 dict O(1)
        deadends = set(deadends)
        if '0000' in deadends:
            return -1        
        deadends.add('0000')
        q = Queue()
        q.put(('0000',0)) #设计一个双元素的队列

        while not q.empty():
            node, step = q.get()

            for i in range(4):
                for add in (-1,1):
                    temp = node[:i] + str((int(node[i])+add)%10) + node[i+1:]
                    if temp == target:
                        return step+1
                    if temp not in deadends:
                        q.put((temp,step+1))
                        deadends.add(temp)
        return -1

if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    
    s = Solution()
    print(s.openLock(deadends,target))
