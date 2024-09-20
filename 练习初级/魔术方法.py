class student:


    def __init__(self,Name,Age):
        self.Name=Name
        self.Age =Age
    def __str__(self): # 改变内置方法 #内存地址 ———>字符串
        return f"{self.Name,self.Age}"

    # 改变内置方法 #比较方法
    #  def __lt__(self, other):
    #      return self.Age>other.Age
    #
    # def __le__(self, other):
    #     return self.Age <= other.Age

    def __eq__(self, other):
        return self.Age==other.Age

Stu=student("刘淼",3)
Stu2=student("淼淼",23)
print(Stu)  #内存地址  ———>字符串
print(Stu2)  #内存地址 ———>字符串

print(Stu==Stu2)
print(Stu==Stu2)