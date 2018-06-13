
# Reverse a string

str_var = "Rita"
print(str_var[::-1])

# Write a sorting algorithm for a numerical dataset in Python

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)


def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        # print(sChild)
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print("sChildPath",sChildPath)


print_directory_contents("D:\Ritu_Content\SelfStudy\Python\Practice_Scripts\Python_Concepts")

def f(*args,**kwargs): print(args, kwargs)

f()
f(1,2,3)
f(1,2,3,'ritu')
f(a=1,b=2,c=3)

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list[1:3])


dict_var = {'uyu':4,'yty':4,'rty':89}

for key in dict_var:
    print(key)
    print(dict_var.keys())
    print(dict_var.values())

class X(object):
    def __init__(self, a):
        print("Class X __init__")
        self.num = a

    def doubleup(self):
        print("Class X doubleup")
        self.num *= 2


class Y(X):
    def __init__(self, a):
        print("Class Y __init__")
        X.__init__(self, a)

    def tripleup(self):
        print("Class Y Tripleup")
        self.num *= 3

print("""==================""")
obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)

# ritu Chawla   ritu Chawla ritu
# ritu Chawla  ritu Chawl ritu
strVar = " ritu Chawla"
strVar1 = strVar[:-1]
print(strVar, strVar1,"ritu")
