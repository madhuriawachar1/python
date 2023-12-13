'''#create dictionary

dict1={}

for i in range(10):
    dict1[i]=i+10
print(dict1)




'''

'''def firstElementKTime(self,  a, n, k):
        # code here
        counter = dict.fromkeys(a, 0)
      
        for item in a:
            counter[item] += 1
            if counter[item] >= k:
                return item
        
            
        return -1'''
                
def firstElement(arr, n, k):
 
    # dictionary to count
    # occurrences of
    # each element
    count_map = {}
    for i in range(0, n):
        if(arr[i] in count_map.keys()):
            count_map[arr[i]] += 1
        else:
            count_map[arr[i]] = 1
        i += 1
    print(count_map)
    for i in range(0, n):
         
        # if count of element == k ,
        # then it is the required
        # first element
        if (count_map[arr[i]] == k):
            return arr[i]
        i += 1
             
    # no element occurs k times
    return -1
 
# Driver Code
if __name__=="__main__":
 
    arr = [1, 7, 4, 3, 4, 8, 7];
    n = len(arr)
    k = 2
    print(firstElement(arr, n, k))


d = {1: '001', 2: '010', 3: '011'}
# since 4 is not in keys, it'll print "Not found"
print(d.get(4))

print(d.get(4, "Not found"))
