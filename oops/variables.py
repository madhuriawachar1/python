class car:
    #static var or class var
    #same for all objects
   
    wheels=4
    def __init__(self):
        #instance var
        #different for different objects
        self.mil=10
        self.com='BMW'
    def pf(self):
        print(self.mil,self.com,self.wheels)
        
c1=car()
c2=car()
print('before change') 
c1.pf()   
c2.pf()
print('after change static for 1 obj')
c1.wheels=5
print(c1.wheels)
print(c2.wheels)
c1.mil=8
c1.pf()   
c2.pf()
car.mil=9
car.wheels=22
print('after change in static var') 
c1.pf()   
c2.pf()
c3=car()
print(car.mil)
print(c3.mil)

print(vars(c3))
print(vars(car))
      