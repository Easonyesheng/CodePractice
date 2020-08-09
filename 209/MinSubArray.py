"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        '''积分数组

        '''
        if not nums: return 0

        # get sum array
        sum_nums = [0]
        for i in range(len(nums)):
            temp = sum_nums[i] + nums[i]
            sum_nums.append(temp)
        
        for i in range(1,len(sum_nums)):
            for j in range(len(sum_nums)-i):
                if (sum_nums[j+i] - sum_nums[j])>=s:
                    return i
        
        return 0


if __name__ == "__main__":
    S = Solution()
    s = 7
    nums = [2,3,1,2,4,3]
    print(S.minSubArrayLen(s,nums))


            

            