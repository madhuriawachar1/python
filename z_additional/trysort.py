sorted([2,3,1,5,4,6])#won't print anything

print(sorted([2,3,1,5,4,6]))# will print the sorted list


a=[1,2,3,4,5,6]
sorted(a,reverse=True)
print(a)# will print the original list
sorted_list_desc = sorted(a, reverse=True)
print(sorted_list_desc)# will print the sorted list in descending order


print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
#key function
a=sorted(student_tuples, key= lambda students: student_tuples[1])   # sort by a
print(a)


