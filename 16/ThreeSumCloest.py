"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 左右边界双指针

class Solution:
    def threeSumClosest(self, nums: list(int), target: int) -> int:
        nums_sort = sorted(nums)
        res = 0
        for i in range(len(nums)-2):
            L = i+1
            R = len(nums)-1
            res = nums_sort[i] + nums_sort[L] + nums_sort[R]
            if res == target: return res
            