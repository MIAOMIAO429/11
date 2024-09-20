class student:


    def __init__(self,Name,Age,Dizhi):
        self.Name=Name
        self.Age =Age
        self.Dizhi=Dizhi
Stu=[]
for i in range(1,4):
    Stu = student(Name=(input("请输入名字:")),Age=(input("请输入年龄:")),Dizhi=(input("请输入地址:")))
    print(f"{Stu.Name} {Stu.Age} {Stu.Dizhi}")

