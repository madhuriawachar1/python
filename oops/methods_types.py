class student:
    schoolname="bpschool"
    def __init__(self):
        self.name='madhuri'
        self.age=22
        self.marks=90
        
        
    #instance methods
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name=name
    
    @classmethod
    def get_school(cls):
        return cls.schoolname
    
    @staticmethod
    def info():
        print('this is student class')
    
s1=student()
#instance methods works with obj name and class name
print(s1.get_name())
s1.set_name('madhu')
print(s1.get_name())
student.set_name(s1,'akash')
print('after change class name to akash change in obj name')

print(s1.get_name())

#class methods works with obj name and class name
print(student.get_school())
print(s1.get_school())

student.info()
s1.info()