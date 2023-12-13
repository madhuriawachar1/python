class person:
    def __init__(self,name):
        self._name=name
    
        
class emp(person):
    def __init__(self,name,eno):
        self.eno=eno
        person.__init__(self,name)
        
    def details(self):
        print('details',self._name,self.eno) 
    def pf(self):
        print(self._name)
        
e=emp('madhuri',101)   


e.details()