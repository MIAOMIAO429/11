""""
n1={"liumiao","222","222"}
n2=["liumiao","222","222"]

print(n2)
n1.add("刘淼")
n3=n1.pop()
print(n1)
print(n3)


str3=str1.difference_update(str2)
print(str2)
print(str1)

str1={1,2,3,}
str2={1,5,6}

str3={1, 2, 3, 5, 4,6}

for x in str3:
    print(x)
    
"""""
my_list =["黑马程序员","黑马程序员","黑马程序员","黑马程序员","liumaio","liumaio","liumaio"]
set1=set(my_list)
print(set1)
print(type(set1))
list1=list(set1)
print(list1)
print(type(list1))