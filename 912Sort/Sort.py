"""
给你一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Quick sort
import random

class Solution:
    def sortArray(self, nums: list) -> list:
        '''
        '''
        self.recursive_quick_sort(nums, 0, len(nums)-1)
        return nums
    
    def quick_sort(self, nums, l, r):
        '''Quick sort implement
        :para
            l: low boundry
            r: high boundry
            nums: list
        :output
            pivot: the index of pivot
        '''
        
        # get pivot
        pivot = random.randint(l,r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        
        i = l-1
        for j in range(l,r):
            if nums[j] <= nums[r]:
                i+=1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1

    def recursive_quick_sort(self, nums, l, r):
        '''recursive part
        '''
        if r <= l: return
        pivot = self.quick_sort(nums, l, r)
        self.recursive_quick_sort(nums, l, pivot-1)
        self.recursive_quick_sort(nums, pivot+1, r)
    

if __name__ == "__main__":
    s = Solution()
    nums = [5,1,1,2,0,0]
    print(s.sortArray(nums))