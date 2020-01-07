class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_list = []
        for i in range(1, n + 2):
            if i == 1:
                fib_list.append(1)
            elif i == 2:
                fib_list.append(2)
            else:
                fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list[n - 1]
