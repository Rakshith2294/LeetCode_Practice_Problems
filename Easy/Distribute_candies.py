class Solution(object):
    def frequency(self,var_list):
        dict_var = {}
        for i in var_list:
            if i in dict_var:
                dict_var[i]+=1
            else:
                dict_var[i]=1
        return dict_var
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        freq=self.frequency(candies)
        if len(freq) > len(candies)/2:
            return len(candies)/2
        else:
            return len(freq)
