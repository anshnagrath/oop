class A:
    def hi(self):
        print('class A')
    def another(self):
        print('in class A')
class B(A):
    def hi(self):
        print('class B')
class C:
    def hi(self):
        print('classC')

class D(B,C):
    pass



t=D()
t.hi()
t.another()

