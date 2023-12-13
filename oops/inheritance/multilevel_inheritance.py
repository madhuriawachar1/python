class Grandfather:
    def __init__(self, grandfathername):
        print('Grandfather name ')
        self.grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        print('Father name ')
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        print('Son name ')
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name:', self.grandfathername)
        print("Father name:", self.fathername)
        print("Son name:", self.sonname)


# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
