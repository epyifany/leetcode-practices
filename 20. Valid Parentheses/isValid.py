class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_stack = list()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                a_stack.append(c)
            elif c == ")":
                if len(a_stack) == 0 or a_stack.pop() != "(":
                    return False
            elif c == "]":
                if len(a_stack) == 0 or a_stack.pop() != "[":
                    return False
            elif c == "}":
                if len(a_stack) == 0 or a_stack.pop() != "{":
                    return False
        if len(a_stack) == 0:
            return True
        else:
            return False
