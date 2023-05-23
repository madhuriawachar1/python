class person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        
    def details(self):
        print(self.name+' '+self.lastname)
class student(person):
    pass

a=student('Madhuri','Awachar')
a.details()
        
        
        
        
       