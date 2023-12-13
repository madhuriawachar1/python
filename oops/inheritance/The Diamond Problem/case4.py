class A:
    def m(self):
        print("m of A called")
class B(A):
    pass
class C(A):
    def m(self):
        print("m of C called")
class D(B,C):
    pass
x = D()
x.m()


class X(object):
    def m(self):
        print("m of A called")
class Y(X):
    pass
class Z(X):
    def m(self):
        print("m of C called")
class S(Y,Z):
    pass
x = S()
x.m()