
class Person:

	
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber
	    
		self._a=2
  		
	def print_name(self):
		print(self.name)
		print(self.idnumber)
		print(self._a)
	def display(self):
		print('hrlp')
# child class
class Employee(Person):
	def __init__(self, salary, post,a):
		self.salary = salary
		self.post = post
		self._a=a
		print(self._a)	
  

		# invoking the __init__ of the parent class
		#Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee(200000, "Intern",3)
a.display()

a.print_name()
# calling a function of the class Person using its instance

