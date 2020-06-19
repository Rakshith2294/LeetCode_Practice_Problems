class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        var_dict = {}
        var_dict['}']='{'
        var_dict[')']='('
        var_dict[']']='['
        stack = list()
        for i in s:
            if i in var_dict.values():
                stack.append(i)
            else:
                if len(stack) !=0:
                    if var_dict.get(i) == stack[len(stack)-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        
