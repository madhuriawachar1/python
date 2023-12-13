#when parent class hv constructor but child class not hv constructor

class A:
    def __init__(self):
        print('in A init')
    
        
        
class B(A):
    def feature1(self):
        print('feature 1 working')
        

a=A()

b=B()
