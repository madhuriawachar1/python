l1=[1,2,5,8,7,4,3,6,9]

for i in range(3):
    l1.append(l1.pop(0))
    
print(l1)
l1.reverse()

print('after reversingl1.reverse() ',l1)

l1=[1,2,5,8,7,4,3,6,9]
l2=l1
l2[0]=10
print(l1)
print(l1.count(10))


import copy
l1=[1,2,5,8,7,4,3,6,9]
l2=copy.copy(l1)
l2[0]=10
print('how copy works')
print(l1)
print(l2)
for i in range(0,len(l1)):
    print (l1[i],end=" ")
 
l1[0]=20
print('copy',l2)   

import copy
l1=[1,2,5,8,7,4,3,6,9]
l2=copy.deepcopy(l1)
l2[0]=10
print(l1)
l1[0]=20
print('copy',l2)   

import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
    
print('clear')  
ls=[1,2,3,4,5,6,7,8,9]
print(ls.clear())
print(ls)

lis_1 = [1, 3, 5]
 
lis_2 = [7, 9, 11]
 
# using clear method
lis_1.clear()
print("List after using clear():", lis_1)
 
# using del to clear items
del lis_2[1:]
print("List after using del:", lis_2)

print('count')
ls=[1,1,2,3,4,3,2,1,23,4]

a=ls.count(1)
print('occurence of 1:',a)

print('extend')
print('beore extend')
print(ls)
ls.extend(lis_2)
print('after extend')
print(ls)


print('index')
print(ls.index(1))
ls.insert(0,100)
print(ls)
ls.remove(100)
print(ls)

print(ls.reverse())
print(ls)
print(ls[::-1])

print('Reversing a sublist using Slicing')

my_list = [1, 2, 3, 4, 5]
print('Original list:', my_list)
my_list[1:4] = my_list[1:4][::-1]
print('Reversed sublist:', my_list)