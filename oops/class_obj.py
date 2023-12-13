#declare class obj public,private,protected


class comp:
    #Python does not support constructor overloading. If you try to overload the constructor, the last implementation will be executed each time. Any previous implementation will be over-written by the latest one.
    def __init__(self):
        self._a=2
        self.b=3
        self.__c=4
        print('base constructor')
        
        
        
    '''def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("Base class A constructor")'''
    def config(self):
        print("i5, 16gb, 1TB")
    def getp(self):
        return self.__c
    
    
    
class derive(comp):
    def __init__(self):
        

        print('derived constructor')        
#calling class        
c1=comp() #will call the last constructor hence error as last constructor has 2 arguments
#c2=comp('i5',16) 
 
c1.config()
comp.config(c1)
#print(c1._a)
print('for  c1.__c  we get error AttributeError: comp object has no attribute __c')
print('access private member with getter',c1.getp())

print('derived class')
d1=derive()
d1.config()
print(c1._a)


