class Solution:
    def noOfWays(self, m: int, n: int, x: int) -> int:
        dp = [0] * (x + 1)
        dp[0] = 1 
        for _ in range(n):
           
            for s in range(x, 0, -1):
                ways = 0
               
                for face in range(1, min(m, s) + 1):
                    ways += dp[s - face]
                dp[s] = ways
        
        return dp[x]

sol = Solution()

print(sol.noOfWays(6, 3, 12))   # Output: 25
print(sol.noOfWays(2, 3, 6))    # Output: 1
print(sol.noOfWays(6, 2, 7))    # Output: 6
print(sol.noOfWays(4, 3, 5))    # Output: 6
print(sol.noOfWays(6, 1, 1))    # Output: 1
print(sol.noOfWays(6, 1, 7))    # Output: 0