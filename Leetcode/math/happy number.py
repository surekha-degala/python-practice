class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.help(n)
        return n ==1
    def help(self, n):
            sum =0
            while (n >0):
                digit = n %10
                sum += digit *digit
                n = n/10
            return sum
