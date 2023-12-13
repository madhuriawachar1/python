def selection(l):
    n=len(l)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if l[j]<l[mini]:
                mini=j
                
        l[i],l[mini]=l[mini],l[i]
    print(l)    
l=[2,4,1,5,3]
selection(l)
