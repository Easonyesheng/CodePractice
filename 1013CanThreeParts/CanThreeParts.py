"""
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 牛顿-莱布尼茨公式

class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        '''
        '''
        # get the sum list
        SumA = []
        SumA.append(0)
        for i in range(len(A)):
            temp = SumA[i] + A[i]
            SumA.append(temp)
        
        # print("Sum:  ",SumA)
        #judge
        L = len(A)
        if L < 3:
            return False

        F_i_plus_1 = SumA[L]/3
        F_j_plus_1 = F_i_plus_1*2
        # print('F(i+1) %d , F(j+1) %d' %(F_i_plus_1,F_j_plus_1))

        SumA_cut = SumA[1:L]

        if not F_i_plus_1 in SumA_cut:
            return False
        else:
            i_plus_1 = SumA_cut.index(F_i_plus_1)+1
            # print("i+1 %d" %i_plus_1)

        if not F_j_plus_1 in SumA_cut:
            return False
        else:
            temp_SumA = SumA_cut[::-1]
            # print(temp_SumA)
            j_plus_1 = L-temp_SumA.index(F_j_plus_1)-1
            # print("j+1 %d" %j_plus_1)

        if i_plus_1 >= j_plus_1:
            return False
        
        return True
    
if __name__ == "__main__":
    s = Solution()
    L = [6,1,1,13,-1,0,-10,20]
    print(s.canThreePartsEqualSum(L))
    
