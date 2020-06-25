class Solution(object):
    def frequency(self,var_list):
        dict_var = {}
        for i in var_list:
            if i in dict_var:
                dict_var[i]+=1
            else:
                dict_var[i]=1
        return dict_var

    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text_needed = list()
        text_needed = ['b','a','l','o','n']
        word_freq = self.frequency(text)
        for i in text_needed:
            if i not in word_freq.keys():
                return 0
        return min(word_freq['b'],word_freq['a'],word_freq['l']/2,word_freq['o']/2,word_freq['n'])
