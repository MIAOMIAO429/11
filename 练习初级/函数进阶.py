"""""
def test1():
    return 1,"s","one"

x,y,z=test1()
print(f"{x} {y} {z}")


def test2(name,age,sex="男"):
    print(f"姓名{name} 年龄{age} 性别{sex}")
test2(age=20,name="刘淼")

def test3(*args):
    print(args)
test3("刘淼")
test3("刘淼",18,"100W")


def test4(**kwargs):
    print(kwargs)

test4(name="刘淼",age=18,ID=666)

def add(x,y):
    return x+y
def test5(add,x,y):
    SUM=add(x,y)
    print(SUM)

test5(add,14,4)
"""""
# def ADD(x,y):
#     return x+y
def test7(ADD):
    sum1=ADD(1,2)
    print(sum1)
test7(lambda x,y:x-y)
test7(lambda x,y:x+y)