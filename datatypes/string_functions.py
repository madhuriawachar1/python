a='hell0123 i am Madhuri Awachar'


#count
#string_name.count(char or word which u eant to count)  Return the number of times the value "apple" appears in the string:
a.count('l')
print('occurance of l in above sentence',a.count('l'))




#endswith Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)



#index() and find()
txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))





#format
txt="my name is {} and my age is {}".format('madhuri',22)
print(txt)


#check for all
# if all characters 
txt = "Company12"
txt1='asd123@'
x = txt.isalnum()
y=txt1.isalnum()
print(x,y)



#all digits, all alphabets or all decinal means no float or it may ve unicode va like a = "\u0030"
txt = "Company12"
print(txt.isalpha(),txt.isdigit(),txt.isdecimal())


#split and join

#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.

#Syntax
#string.join(iterable)
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)




#replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#split
txt = "welcome to the jungle"

x = txt.split()

print(x)

'''1.string.endswith(value, start_index, end_index within to search) return true or false


2.string_name.count(char or word which u eant to count)
3.string.find(value, start, end) return index of first occurance of value give -1 if not found
4.string.index(value, start, end) return index of first occurance of value give error if not found
5.string.isalnum() return true if all characters are alphanumeric
6.
'''