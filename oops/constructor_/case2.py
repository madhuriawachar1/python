#when parent class hv constructor but child class not hv constructor

from typing import Any


class A:
    def __init__(self):
        print('in A init')
    
        
        
class B(A):
    def __init__(self):
        print('in B init')
        
        #if we want to call parent class constructor then we have to use super keyword
        super().__init__()
    def feature1(self):
        print('feature 1 working')
        

a=A()

b=B()
