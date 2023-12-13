#User function Template for python3
import sys
import math
class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        
        
        dp = [-1] * n
        def find(ind,height,dp):
            
            if ind == 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            jumpTwo = sys.maxsize
            jumpOne = find(ind-1, height, dp) + abs(height[ind] - height[ind-1])
            if ind > 1:
                jumpTwo = find(ind-2, height, dp) + abs(height[ind] - height[ind-2])
            dp[ind] = min(jumpOne, jumpTwo)
            return dp[ind]
        return find(n-1,height,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends