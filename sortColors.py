class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        flag = 0
        while i<len(nums)-1:
            if nums[i+1] == 0:
                nums[i],nums[i+1] = nums[i+1], nums[i]
                i+=1
            if nums[i] == 2 and flag < 2*i:
                nums[i+1],nums[i] = nums[i], nums[i+1]
                flag += i
            else :
                i+=1
                flag =0
            if nums[i] == 1:
                i+=1
