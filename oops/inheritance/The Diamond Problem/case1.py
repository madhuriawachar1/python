#When every class defines the same method
#depth-first and then left-to-right. If you change the header line of A into "class A(object):", we will have the same behaviour in both Python versions.


# Python Program to depict multiple inheritance
# when every class defines the same method

class Class1:
	def m(self):
		print("In Class1") 
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")	 
	
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
      

obj = Class4()
obj.m()
#Let's apply the method m on an instance of D. We can see that only the code of the method m of D will be executed. We can also explicitly call the methods m of the other classes via the class name,
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
