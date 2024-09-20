"""""
import random

var_1 :int =10
var_2:float=3.1415926
var_3:bool=True
var_4:str="liumiao520"
########################################
class Student:
    print("这是一个类")
    pass
stu:Student=Student()
#################

my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_set:set={1,2,3}
my_dict:dict={"001":"刘淼"}
my_str:str="我叫刘淼"

#————————————————————————————————

list1:list[int]=[1,2,3]
tuple2:tuple[int,str,bool]=(12,"刘淼",True)
dict3:dict[int,str]={1:"刘淼"}

#注释标记类型
eg1=random.random(1,10) #type:int


def he(x:int,y:int):
    return x+y
print(he(1,2))

def func(date:list) ->list:
    return date

print(func([1,2,3]))
"""""
from  typing import Union
my_list:list[Union[int,str]]=[1,2,"刘淼","mm"]

def test(data:Union[int,str]) ->Union[int,str]:
    pass
test()