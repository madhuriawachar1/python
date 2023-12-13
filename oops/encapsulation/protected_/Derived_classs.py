#protectetd
#Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
# demonstrate protected members 

# class Base:
class Base:
    def __init__(self):
        self._a = 2
        self.__b=20
        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        #access base class protected mem
        print("Calling protected member of base class: ",self._a)
        #print("Calling private member of base class: ",self.__b)
        
    def access_private(self):
        print("Calling protected member of base class: ")
        print(self._a)
        self._a=30
        print("Calling private member of base class: ")
        #print(self.__b)
     
        
d1=Derived()
d1.access_private()
d1.access_private()
b1=Base() 
print(b1._a)  


# program to illustrate protected 
# data members in a class 


# super class 
class Shape: 
	
	# constructor 
	def __init__(self, length, breadth): 
		self._length = length 
		self._breadth = breadth 
		
	# public member function 
	def displaySides(self): 

		# accessing protected data members 
		print("Length: ", self._length) 
		print("Breadth: ", self._breadth) 


# derived class 
class Rectangle(Shape): 

	# constructor 
	def __init__(self, length, breadth): 

		# Calling the constructor of 
		# Super class 
		Shape.__init__(self, length, breadth) 
		
	# public member function 
	def calculateArea(self): 
					
		# accessing protected data members of super class 
		print("Area: ", self._length * self._breadth) 
					

# creating objects of the 
# derived class		 
obj = Rectangle(80, 50) 

# calling derived member 
# functions of the class 
obj.displaySides() 

# calling public member 
# functions of the class 
obj.calculateArea() 
