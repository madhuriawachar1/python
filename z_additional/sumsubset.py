#User function Template for python3
class Solution:
    def check(self,i,sum,arr,N,ans):
        if i==N:
            ans.append(sum)
            return
        
        self.check(i+1,sum+arr[i],arr,N,sum)
        self.check(i+1,sum,arr,N,sum)
        
        
	def subsetSums(self, arr, N):
		# code here
		ans=[]
		self.check(0,0,arr,N,ans)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends