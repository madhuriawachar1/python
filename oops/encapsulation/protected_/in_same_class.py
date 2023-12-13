class square:
    def __init__(self,a):
        self._a=a
        self.__b=20
        print(self._a)
        
    def show(self):
        print('area of sqaure',self._a*self._a)
        print('area of sqaure',self.__b*self.__b)
   
s1=square(10)
s1.show()