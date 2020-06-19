class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in val_to_index:
                return [val_to_index[target - nums[i]], i]
            val_to_index[nums[i]] = i
        return [-1, -1]
