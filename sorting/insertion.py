def insertion(l):
    n=len(l)
    for i in range(n):
        j=i
        while(j>0 and l[j-1]>l[j]):
            l[j],l[j-1]=l[j-1],l[j]
            j=j-1
        print(l)   
l=[4,3,2,1]
insertion(l)
