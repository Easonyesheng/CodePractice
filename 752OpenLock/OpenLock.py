"""LeetCode 752
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：

 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 

每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
"""

# 这是一种宏观考虑转向的做法，好像行不通
class Solution:
    def openLock(self, deadends, target) :
        '''main part for solution
            :para
                deadends : the list that we cannot be same
                target : the right number we need to get
            :output
                stride : how many rotation we need to open the lock 
        '''
        if target in deadends or '0000' in deadends:
            return -1


    def gene_rota(self, direction, target):
        '''generate the rotation method with min stride
            :para
                direction : how to rotate, if None, it's free
                target : the target numbers

            :output
                rotation{
                    'min_stride' : int
                    'rota_direction' : [True or False,.,.,.] -> [0->9 or 9->0,.,.,.] 
                    'stirde_delta' : [different directions' stride delta,.,.,.]
                    # 'change' : int - how many numbers need to change the rotation direction
                }
        '''
        rota_direction = []
        stirde_delta = []
        min_stride = 0

        for i in range(4):
            if direction[i] == None:
                if target[i] == '0':
                    rota_direction.append(False)
                    stirde_delta.append(-1) # -1 means this target is 0 , no need to rotate
                elif int(target[i]) > 5:
                    rota_direction.append(False)
                    stirde_delta.append(2*int(target[i])-10)
                    min_stride += (10-int(target[i]))
                else:
                    rota_direction.append(True)
                    stirde_delta.append(10-2*int(target[i]))
                    min_stride += (int(target[i]))
            else:
                rota_direction.append(direction[i])
                stirde_delta.append(abs(10-2*int(target[i])))
                if direction[i]:
                    min_stride += (int(target[i]))
                else:
                    min_stride += (10-int(target[i]))
        
        rotation = {
            'min_stride' : min_stride,
            'rota_direction' : rota_direction,
            'stride_delta' : stirde_delta,
        }
        return rotation

    def check_dead(self, rotation,deadends,target):
        '''check the dead match
            :para
                rotation : rotation information
                deadends : dead list
                target : target number
            :output
                match : True means match
        '''
        match = False
        for j in range(len(deadends)):
            for i in range(4):
                if rotation['rota_direction'][i] and deadends[j][i] > target[i]:
                    break
                if not rotation['rota_direction'][i] and deadends[j][i] < target[i]:
                    break
                match = True
                return match
        return match



if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    direction = [None]*4
    s = Solution()
    rotate = s.gene_rota(direction, target)
    m = s.check_dead(rotate,deadends,target)
    print(m)
