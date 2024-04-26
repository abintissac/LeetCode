class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        week = n // 7
        remainder = n % 7
        total += (28 * week) + (7 * week * (week - 1) // 2)
        total += (week + 1) * remainder + remainder * (remainder - 1) // 2

        return total


n = 10
solution = Solution()
result = solution.totalMoney(n)
print(result)
