class Base1(object):
    def __init__(self,a):
        self.str1 = "Madhuri"
        print("Base1")
        self.a=a
	    
  
  
          
		


class Base2(object):
	def __init__(self):
		self.str2 = "vijaya"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self,a):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self,a)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived('a')
ob.printStrs()
