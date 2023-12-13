#User function Template for python3



def stockBuySell(price, n):
    # code here
    if n==1:
        return
    ans=[]
    i=0
    while(i,n-1):
        
        p=[]
        while(i<n-1 and price[i+1]<=price[i]):
            i+=1
        if (i == n - 1):
            
            
            break
        buy=i
        i+=1
        
        while(i<n and price[i]>=price[i-1]):
            i += 1
        
        sell=i-1
        p.append(buy)
        
        ans.append(p)
    if len(ans)==0:
        print('No Profit')
        
    for i in ans:
        print("("+str(i[0])+' '+str(i[1])+")",end=' ')
        print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        price=list(map(int, input().split()))
        stockBuySell(price, n)
# } Driver Code Ends