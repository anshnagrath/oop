class MyClass:
    pass
x = MyClass()
try:
    x.prorp
except AttributeError:
    print("attr error") 
       

