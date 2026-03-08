class Solution:
    def noOfWays(self, m, n, x):
        dp = [0] * (x + 1)
        dp[0] = 1
        
        for _ in range(n):
            # Go backwards so we use previous die's values
            for s in range(x, 0, -1):
                ways = 0
                for f in range(1, min(m, s) + 1):
                    ways += dp[s - f]
                dp[s] = ways
        
        return dp[x]