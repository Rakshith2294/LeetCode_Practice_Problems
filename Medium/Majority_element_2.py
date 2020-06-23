class Solution(object):
    def frequency(self,list_var):
        dict_var = {}
        for item in list_var:
            if item in dict_var:
                dict_var[item]+=1
            else:
                dict_var[item]=1
        return dict_var

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        freq = self.frequency(nums)
        print freq
        for key,value in freq.items():
            if value > len(nums)/3:
                result.append(key)
            else:
                continue
        return result 
