class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        if n == 1:
            return True
        while n != 1:
            L = [int(i)**2 for i in str(n)]
            n = sum(L)
            if n == 1:
                return True
            if n not in d.keys():
                d[n] = 1
            else:
                d[n] = d[n] + 1
            if d[n] > 1:
                break
        return False
