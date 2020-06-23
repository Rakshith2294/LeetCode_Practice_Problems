class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 2:
            len_nums = len(nums)
            nums.sort()
            for i in range(0,len_nums):
                if nums[len_nums/2] == nums[(len_nums/2)+1]:
                    return nums[len_nums/2]
                else:
                    return nums[(len_nums/2)-1]
        else:
            return nums[0]
