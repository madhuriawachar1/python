class student:
    schoolname="bpschool"
    def __init__(self):
        self.name='madhuri'
        self.age=22
        self.marks=90
        self.lap=self.laptop()
    def show(self):    
        print(self.name,self.age,self.marks)
        self.lap.show()#notice how to call inner class method in parent class
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
            
        def show(self):
            print(self.brand,self.cpu,self.ram) 
            
s1=student()
print('create outer class obj')
s1.show()
#s1.show() error
print('access inner class menthod by outer class')
s1.lap.show()


#create inner class obj
print('create inner class obj')
#lap1=student.lap.....obj.innerclass not class.innerclass
lap1=s1.lap
lap1.show()

lap2=student.laptop()
lap2.show()