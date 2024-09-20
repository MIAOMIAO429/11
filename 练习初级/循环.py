# while(条件)：
'''''
i=0
while i<20:
    print("我的屠龙刀")
    i+=1

#1-100和
sum=0
i=0
while i<=100:

    sum+=i
    i+=1
print(sum)


#九九乘法表
i=1
j=1
while i<=10:
    j=1
    print(f"{i}天")
    i+=1
    while j<=10:
        print(f"{j}朵玫瑰")
        j+=1


#for 遍历循环
Name="itheima is a brand of itcast"
count=0
for X in Name:
    print(X)
    x=X
    if x=="a":
        count+= 1

print(f"{Name}中有{count}个a")


#偶数奇数个数
count=0
for x in range(200):

    if x%2==0:
        count+=1

print(count)


for x in range(1,3):
    print(f"{x}天               ")
    for y in range(1,11):
        print(f"{y}朵")

'''


