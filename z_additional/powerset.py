#User function Template for python3

class Solution:
    def generate(self,s,st,ans):
        if len(s)<0:
            return
        for i in range(len(s)):
            st+=s[i]
            ans.append(st)
            self.generate(s,st,ans)
	def AllPossibleStrings(self, s):
		# Code here
		ans=[]
		st=''
		self.generate(s,st,ans)
		return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends