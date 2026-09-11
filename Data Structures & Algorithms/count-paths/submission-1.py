class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(m - 1):
            tmp = [1] * n
            for j in range(n - 2, -1, -1):
                tmp[j] = tmp[j + 1] + dp[j]
            dp = tmp
        return dp[0]
                