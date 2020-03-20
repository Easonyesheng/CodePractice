"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""

# 快速排序

class Solution:
    def getLeastNumbers(self, arr, k: int):
        '''Door
        '''
        if (not arr) : return []
        if k == 0: return []

        lo = 0
        hi = len(arr) - 1
        return self.__search_k(arr,lo,hi,k-1)

    def __search_k(self, arr, lo, hi, k):
        '''search the least k by fast sort
        :para
            arr : array
            lo : low boundry
            hi : high boundry
            k : need to find k+1 least nums
        :output
            arr[:k+1]
        '''
        j = self.__fast_sort(arr,lo,hi)
        if j == k :
            return arr[:k+1]
        else:
            return self.__search_k( arr,lo,j-1,k) if j > k  else self.__search_k(arr,j+1,hi,k)

    def __fast_sort(self, nums, l, r):
        ''''apply fast sort on nums[l:r]
        用最后一个元素作为切分值，最后切分值放在【i+1】
        :para
            arr : array
            l : low boundry
            r : high boundry
        :output
            j : arr[i<j] < arr[j] < arr[k>j]
        '''
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    # def __fast_sort(self, arr, lo, hi):
    # 超时
    #     '''apply fast sort on arr[lo:hi]
    #     :para
    #         arr : array
    #         lo : low boundry
    #         hi : high boundry
    #     :output
    #         j : arr[i<j] < arr[j] < arr[k>j]
    #     '''
    #     pos = arr[lo]
    #     i = lo 
    #     j = hi + 1
    #     while(True):
    #         while(i <= hi and arr[i] < pos):
    #             i += 1
    #         while((j-1) >= lo and arr[j-1] > pos):
    #             j -= 1
    #         if i >= j: 
    #             break
    #         arr[i],arr[j] = arr[j],arr[i]
    #     arr[j], arr[lo] = arr[lo], arr[j]
    #     return j
    

if __name__ == "__main__":
    s = Solution()
    arr = [0,0,1,2,4,2,2,3,1,4]
    k = 8
    print(s.getLeastNumbers(arr,k))