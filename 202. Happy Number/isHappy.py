class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = list()
        num = n
        while n not in a:
            a.append(n)
            new_sum = 0
            for c in "{}".format(n):
                c_num = int(c)
                new_sum += c_num * c_num
            if new_sum == 1:
                return True
            n = new_sum

        return False
