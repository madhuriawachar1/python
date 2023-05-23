def quickSort(arr,low,high):
        # code here
        if(low<high):
            part=partition(arr,low,high)
            quickSort(arr,low,part-1)
            quickSort(arr,part+1,high)
        #print(arr)
def partition(arr,low,high):
    # code here
    #select pivot
    pivot=arr[low]
    #select i and j position for comaparison
    i=low +1
    j=high
    while(i<=j):#do it till i<=j
        while(arr[i]<arr[pivot] and i<=high-1):
            i+=1
        while(arr[j]>arr[pivot] and j>=low+1):
            j-=1   
        if(i<j):    
            arr[i],arr[j]=arr[j],arr[i]
    arr[pivot],arr[j]=arr[j],arr[pivot]
    
    
    return i

quickSort([4, 1, 3, 9, 7],0,4)