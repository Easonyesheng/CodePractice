"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# math question

from math import floor, sqrt

class Solution:
    def findContinuousSequence(self, target: int):
        '''force + math
            for i 
                find sum(a,a+1,...,a+interval) = target
                if interval is a integer
                get the list
                else continue
        '''
        sequence = []
        for i in range(1,target-1):
            interval = (sqrt((2*i+1)**2-8*(i-target))-(2*i+1))/2
            if interval == floor(interval):
                temp = []
                for a in range(i,i+int(interval)+1):
                    temp.append(a)
                sequence.append(temp)
            else:
                continue
        return sequence

if __name__ == "__main__":
    s = Solution()
    print(s.findContinuousSequence(15))