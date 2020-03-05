"""
排排坐，分糖果。

我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies-to-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 数学问题 -- 理解错误

from math import sqrt, ceil, floor
import numpy as np 

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        '''math question

        '''

        # get the children's list
        children = np.ones((1,num_people),dtype=np.int)
        for i in range(num_people):
            children[0][i] *= (i+1)
        print('ori:',children[0])

        # one loop we need candies
        need_candies_1loop = (1+num_people)*num_people/2

        # max loop times we get
        max_loop_times = floor(candies/need_candies_1loop)
        print('max pool times:',max_loop_times)

        # intergreted loop done we get candies
        children = children * max_loop_times
        print("intergreted loop done:",children[0])

        # left candies
        left_candies = candies % need_candies_1loop 
        print("left candies:",left_candies)

        # the last child who can get candies
        last_child = ceil((sqrt(1+8*left_candies)-1)/2)
        print("last child:",last_child)

        # last child can get how many candies
        last_candies = left_candies - (last_child)*(last_child-1)/2 

        # the last loop
        for i in range(last_child-1):
            children[0][i] += (i+1)
        children[0][last_child-1] += last_candies
        # children.squeeze()
        return list(children[0])


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies(10,3))