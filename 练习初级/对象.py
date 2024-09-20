'''''
class Dengjibian:
    name=None
    gender=None   #性别
    age=None
    def dayi(self,msg):
        print(f"{self.name} {self.gender} {self.age} {msg}")
#创建一个对象
stu1=Dengjibian( ) #stu_1 变量 /类
stu1.name="刘淼"
stu1.age=20
stu1.gender="男"

stu1.dayi("大家好") #类 方法


#闹钟
class Clock:
    ID=None
    price=None

    def ring(self):
        import  winsound
        winsound.Beep(2000,3000)#频率 ，时间

clock1=Clock
clock1.ID="001"
clock1.price=100
print(f"编号{clock1.ID} 价格{clock1.price}")
clock1().ring()#铃声

clock2=Clock
clock1.ID="002"
clock1.price=188
print(f"编号{clock2.ID} 价格{clock2.price}")
clock2().ring()#铃声
############################################################################
'''
class student:
    Name = None
    Gender = None  # 性别
    Age = None

    def __init__(self,name,gender,age):
        self.Name=name
        self.Gender=gender
        self.Age =age

stu1=student("刘淼",30,"男")

print(f"{stu1.Name,stu1.Gender,stu1.Age}")