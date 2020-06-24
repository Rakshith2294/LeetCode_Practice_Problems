class Solution(object):

    def frequency(self,list_var):
        dict_var = {}
        for item in list_var:
            if item in dict_var:
                dict_var[item]+=1
            else:
                dict_var[item]=1
        return dict_var

    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        list1_dict = {}
        list2_dict = {}
        result = list()
        list1=A.split()
        list2=B.split()
        list1_dict = {}
        list2_dict = {}
        list1_dict = self.frequency(list1)
        list2_dict = self.frequency(list2)
        for key,value in list1_dict.items():
            if key not in list2_dict and value==1:
                result.append(key)
        for key,value in list2_dict.items():
            if key not in list1_dict and value==1:
                result.append(key)
        return result 
