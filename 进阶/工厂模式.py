''''
class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass


worker=Worker()
stu=Student()
teacher=Teacher()

'''''


from pyspark.daemon import worker


class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

# 使用工厂类的get person()方法去创建具体的类对象优点:
# 大批量创建对象的时候有统一的入口，易于代码维护当发生修改，
# 仅修改工厂类的创建方法即可符合现实世界的模式，即由工厂来制作产品(对象)
class Factory:#工厂模式
    def get_person(self,p_type):
        if p_type=='s':
            return Student
        elif p_type=='w':
            return Worker
        else:
            return Teacher

factory=Factory()
worker=factory.get_person('w')
stu=factory.get_person('s')
teacher=factory.get_person('t')
