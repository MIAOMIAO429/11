'''
str1="Liumiao"
# print(str1[0])
# print(str1[-7])
#
# print(str1.index("miao"))
#替换

print(str1)
str2=(str1.replace("Liu","刘"))
print(str2)

name="liumiao liumiao liumiao "
fengge=name.split(" ")
print(fengge)





name="   liumiao1 liumiao2 liumiao               "
name1=name.strip(" ")
print(name1)

name="123liumiao1 liumiao2 liumiao32121321"
name2=(name.strip("123"))
print(name2)
'''
srt1="iteima itcast boxugu"
count=srt1.count("it")
srt2=srt1.replace(" ","|")
srt3=srt2.split("|")
print(f"{count},{srt2},{srt3}")