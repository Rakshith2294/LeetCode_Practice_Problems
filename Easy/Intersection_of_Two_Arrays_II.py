class Solution(object):
    def frequency(self,list_var):
        dict_var = {} 
        for item in list_var:
            if item in dict_var:
                dict_var[item]+=1
            else:
                dict_var[item]=1
        return dict_var
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()
        nums1_dict = self.frequency(nums1)
        nums2_dict = self.frequency(nums2)
        print nums1_dict,nums2_dict
        if len(nums1_dict)<len(nums2_dict):
            for i in nums1_dict:
                if i in nums2_dict:
                    for j in range(0,min(nums1_dict[i],nums2_dict[i])):
                        result.append(i)
                    
        else:
            for i in nums2_dict:
                if i in nums1_dict:
                    for j in range(0,min(nums1_dict[i],nums2_dict[i])):
                        result.append(i)
                        
        return result 
