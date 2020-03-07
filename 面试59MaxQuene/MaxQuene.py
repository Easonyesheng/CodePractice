"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 只有在set()里面，查找是O(1),其他的查找都是O(n)
# 使用双向队列deque，设置辅助的单调递减队列，保证Max函数O(1)
# 但是同时无法满足push O(1)

from collections import deque

class MaxQueue:

    def __init__(self):
        self.Que = deque()
        self.MaxQue = deque()

    def max_value(self):
        return self.MaxQue[0] if self.MaxQue else -1
       
    def push_back(self, value):
        self.Que.append(value)
        while self.MaxQue and self.MaxQue[-1] < value:
            self.MaxQue.pop()
        self.MaxQue.append(value)
        

    def pop_front(self):
        if not self.Que:
            return -1
        value = self.Que.popleft()
        if value == self.MaxQue[0]:
            self.MaxQue.popleft()
        return value


if __name__ == "__main__":
    que = MaxQueue()
    que.push_back(1)
    que.push_back(2)
    que.push_back(6)
    print(que.Que,'\n',que.max_value())
    que.pop_front()
    que.pop_front()
    
    print(que.Que,'\n',que.max_value())
    que.push_back(4)
    print(que.Que,'\n',que.max_value())
    que.push_back(7)
    print(que.Que,'\n',que.max_value())
