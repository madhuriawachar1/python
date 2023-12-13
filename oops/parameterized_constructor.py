class comp:
    #Python does not support constructor overloading. If you try to overload the constructor, the last implementation will be executed each time. Any previous implementation will be over-written by the latest one.
    def __init__(self):
        self._a=2
        self.b=3
        self.__c=4
        print('base constructor')
        
        
        
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("Base class A constructor")
    def config(self):
        print('congig is',self.cpu,self.ram)
    def getp(self):
        return self.__c


c1=comp('a',5) #will call the last constructor hence error as last constructor has 2 arguments
c1.config() 