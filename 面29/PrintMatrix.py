"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def spiralOrder(self, matrix):   
        out = []
        if not matrix: return out
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                out.append(matrix[0][i])
            return out
        elif len(matrix[0]) == 1:
            for i in range(len(matrix)):
                out.append(matrix[i])
            return out
        else:
            for j in range(len(matrix[0])):
                out.append(matrix[0][j])
            for i in range(len(matrix)):
                out.append(matrix[i][len(matrix[0])-1])
            for j in range(len(matrix[0])-2,-1,-1):
                out.append(matrix[len(matrix)-1][j])
            for i in range(len(matrix)-2,0,-1):
                out.append(matrix[i][0])
            out.extend(self.spiralOrder(matrix[1:len(matrix)-1][1:len(matrix[0])-1]))
            return out

if __name__ == "__main__":
    S = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,2]]
    print(S.spiralOrder(mat))