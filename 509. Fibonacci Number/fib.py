class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fib_list = []
        for i in range(0, N + 1):
            if i == 0:
                fib_list.append(0)
            elif i == 1:
                fib_list.append(1)
            else:
                fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list[N]
