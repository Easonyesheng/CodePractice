"""给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 如果两个数的差能被K整除，就说明这两个数 mod K得到的结果相同

class Solution:
    def subarraysDivByK(self, A, K) -> int:

        Num_array = 0
        if not A: return Num_array

        # get the sum list
        SumA_Mod = []
        SumA_Mod.append(0)
        for i in range(len(A)):
            temp = SumA_Mod[i] + A[i]
            SumA_Mod.append(temp%K)

        SetA = set(SumA_Mod)
        for mod in SetA:
            num = SumA_Mod.count(mod)
            Num_array += (num*(num-1))//2

            

        return Num_array


if __name__ == "__main__":
    S = Solution()
    A = [4,5,0,-2,-3,1]
    K = 5
    print(S.subarraysDivByK(A,K))

